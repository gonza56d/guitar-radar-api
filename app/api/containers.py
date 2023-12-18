from os import getenv

from app.api.repositories.base import SQLRepository
from app.core.api_bus import APICommandBus
from app.core.commands import GetHealthCommand
from app.core.handlers.health import GetHealthHandler
from dependency_injector import containers, providers
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


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=[
        '.routers.health',
        '.routers.components.bridges',
        '.repositories.base',
        '.repositories.bridges',
    ])

    sql_db_url = f'{Env.SQL_IMPL}://{Env.SQL_USER}:{Env.SQL_PASSWORD}@{Env.SQL_SERVICE}/{Env.SQL_DB}'
    sql_engine: Engine = providers.Singleton(
        create_engine,
        url=sql_db_url
    )

    sql_repository: SQLRepository = providers.Factory(
        SQLRepository,
        engine=sql_engine
    )

    bridge_repository: BridgeRepository = providers.Factory(
        BridgeSQLRepository,
        engine=sql_engine
    )

    get_health_handler: GetHealthHandler = providers.Factory(
        GetHealthHandler,
        sql_connection=sql_repository
    )

    command_bus: CommandBus = providers.Factory(
        APICommandBus,
        handlers={
            GetHealthCommand: get_health_handler,
            # CreateBridgeCommand: its_handler
        }
    )
