from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Configuration, Factory, Singleton
from pymessagebus import CommandBus
from pymongo import MongoClient
from sqlalchemy import create_engine, Engine

from app.api.env import Env
from app.api.repositories.health import HealthSQLRepository, HealthMongoRepository
from app.api.repositories.bridges import BridgeSQLRepository
from app.core.api_bus import APICommandBus
from app.core.commands import GetHealthCommand
from app.core.handlers.health import GetHealthHandler
from app.core.repositories.bridges import BridgeRepository
from app.core.repositories.health import HealthRepository


class Container(DeclarativeContainer):

    wiring_config = WiringConfiguration(modules=[
        'app.api.routers.health',
        'app.api.routers.components.bridges',
        'app.api.repositories.base',
        'app.api.repositories.bridges',
    ])
    Configuration()

    sql_db_url = f'{Env.SQL_IMPL}://{Env.SQL_USER}:{Env.SQL_PASSWORD}@{Env.SQL_SERVICE}/{Env.SQL_DB}'
    sql_engine: Singleton[Engine] = Singleton(
        create_engine,
        url=sql_db_url
    )
    mongo_client: Singleton[MongoClient] = Factory(
        MongoClient,
        host=Env.DOCUMENT_HOST,
        port=Env.DOCUMENT_PORT
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

    command_bus: Factory[CommandBus] = Factory(
        APICommandBus,
        handlers={
            GetHealthCommand: Factory(
                GetHealthHandler,
                *health_repositories
            ),
        }
    )
