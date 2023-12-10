from fastapi import FastAPI

from .routers.hello_world import router as hello_world_router


api = FastAPI()
api.include_router(hello_world_router)
