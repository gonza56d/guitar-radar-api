from fastapi import FastAPI

from .routers.hello_world import router as hello_world_router
from .routers.components import router as components_router


api = FastAPI()
api.include_router(hello_world_router)
api.include_router(components_router)
