from fastapi import FastAPI

from .routers.components import router as components_router
from .routers.health import router as health_router


api = FastAPI()
api.include_router(health_router)
api.include_router(components_router)
