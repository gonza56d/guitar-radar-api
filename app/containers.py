from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Configuration, Factory, Singleton
from pymessagebus import CommandBus
from pymongo import MongoClient
from redis import Redis
from sqlalchemy import create_engine, Engine

from app.api.repositories.auth import AuthSQLRepository
from app.api.repositories.brands import BrandSQLRepository
from app.api.repositories.session import SessionTokenRedisRepository
from app.api.repositories.users import UserSQLRepository
from app.core.commands.auth import AuthenticateCommand
from app.core.commands.brands import GetBrandCommand
from app.core.handlers.auth import AuthenticateHandler
from app.core.handlers.brands import CreateBrandHandler, GetBrandHandler
from app.core.handlers.bridges import CreateBridgeHandler
from app.core.repositories.auth import AuthRepository
from app.core.repositories.brands import BrandRepository
from app.core.repositories.session import SessionRepository
from app.core.repositories.users import UserRepository
from app.env import Env
from app.api.repositories.health import HealthSQLRepository, HealthMongoRepository
from app.api.repositories.bridges import BridgeSQLRepository
from app.core.api_bus import APICommandBus
from app.core.commands import GetHealthCommand, CreateBridgeCommand, CreateBrandCommand
from app.core.handlers.health import GetHealthHandler
from app.core.repositories.bridges import BridgeRepository
from app.core.repositories.health import HealthRepository


class Container(DeclarativeContainer):

    wiring_config = WiringConfiguration(modules=[
        'app.api.routers.brands',
        'app.api.routers.health',
        'app.api.routers.components.bridges',
        'app.api.repositories.base',
        'app.api.repositories.bridges',
        # testing
        'tests.utils.sql'
    ])
    Configuration()

    sql_db_url = f'{Env.SQL_IMPL}://{Env.SQL_USER}:{Env.SQL_PASSWORD}@{Env.SQL_SERVICE}/{Env.SQL_DB}'
    sql_engine: Singleton[Engine] = Singleton(
        create_engine,
        url=sql_db_url
    )
    mongo_client: Singleton[MongoClient] = Singleton(
        MongoClient,
        host=Env.DOCUMENT_HOST,
        port=Env.DOCUMENT_PORT
    )
    redis_client: Singleton[Redis] = Singleton(
        Redis,
        host=Env.CACHE_HOST,
        port=Env.CACHE_PORT
    )

    auth_repository: Factory[AuthRepository] = Factory(
        AuthSQLRepository,
        engine=sql_engine
    )

    brand_repository: Factory[BrandRepository] = Factory(
        BrandSQLRepository,
        engine=sql_engine
    )

    bridge_repository: Factory[BridgeRepository] = Factory(
        BridgeSQLRepository,
        engine=sql_engine
    )

    health_repositories: list[Factory[HealthRepository]] = [
        Factory(
            HealthSQLRepository,
            engine=sql_engine
        ),
        Factory(
            HealthMongoRepository,
            client=mongo_client,
            database_name=Env.DOCUMENT_DB
        )
    ]

    session_repository: Factory[SessionRepository] = Factory(
        SessionTokenRedisRepository,
        secret_key=Env.CACHE_SESSION_SECRET_KEY,
        token_expiration_minutes=Env.CACHE_TOKEN_EXPIRATION_MINUTES
    )

    user_repository: Factory[UserRepository] = Factory(
        UserSQLRepository,
        engine=sql_engine
    )

    command_bus: Factory[CommandBus] = Factory(
        APICommandBus,
        handlers={
            AuthenticateCommand: Factory(
                AuthenticateHandler,
                auth_repository=auth_repository,
                user_repository=user_repository,
                session_repository=session_repository
            ),
            GetHealthCommand: Factory(
                GetHealthHandler,
                *health_repositories
            ),
            CreateBrandCommand: Factory(
                CreateBrandHandler,
                brand_repository=brand_repository
            ),
            CreateBridgeCommand: Factory(
                CreateBridgeHandler,
                bridge_repository=bridge_repository
            ),
            GetBrandCommand: Factory(
                GetBrandHandler,
                brand_repository=brand_repository
            )
        }
    )
