from fastapi import FastAPI

from app.api.containers import Container
from app.api.routers.components import router as components_router
from app.api.routers.health import router as health_router


def create_app() -> FastAPI:
    container = Container()
    app = FastAPI()
    app.container = container
    app.include_router(health_router)
    app.include_router(components_router)
    return app


api = create_app()
