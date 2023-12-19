from os import getenv

from app.api.repositories.base import SQLRepository
from app.core.api_bus import APICommandBus
from app.core.commands import GetHealthCommand
from app.core.handlers.health import GetHealthHandler
from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Configuration, Factory, Singleton
from dotenv import load_dotenv
from pymessagebus import CommandBus
from sqlalchemy import create_engine, Engine

from app.api.repositories.bridges import BridgeSQLRepository
from app.core.repositories.bridges import BridgeRepository


load_dotenv()


class Env:
    """Environment variables loaded on api startup."""
    SQL_IMPL = getenv('SQL_IMPL')
    SQL_SERVICE = getenv('SQL_SERVICE')
    SQL_USER = getenv('POSTGRES_USER')
    SQL_PASSWORD = getenv('POSTGRES_PASSWORD')
    SQL_DB = getenv('POSTGRES_DB')


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

    sql_repository: Factory[SQLRepository] = Factory(
        SQLRepository,
        engine=sql_engine
    )

    bridge_repository: Factory[BridgeRepository] = Factory(
        BridgeSQLRepository,
        engine=sql_engine
    )

    command_bus: Factory[CommandBus] = Factory(
        APICommandBus,
        handlers={
            GetHealthCommand: Factory(
                GetHealthHandler,
                sql_connection=sql_repository
            ),
            # CreateBridgeCommand: its_handler
        }
    )
