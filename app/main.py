from http import HTTPStatus

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.api.exceptions import APIException
from app.containers import Container
from app.api.routers.brands import router as brand_router
from app.api.routers.components import router as components_router
from app.api.routers.health import router as health_router
from app.core.exceptions import BusinessException


def include_routers(app: FastAPI) -> None:
    app.include_router(health_router)
    app.include_router(brand_router)
    app.include_router(components_router)


def create_app() -> FastAPI:
    container = Container()
    app = FastAPI()
    app.container = container

    #@app.exception_handler(Exception)
    async def api_exception_handler(request: Request, exc, Exception):
        if isinstance(exc, BusinessException) and isinstance(exc, APIException):
            return JSONResponse(
                status_code=exc.status_code,
                content={'message': exc.message}
            )
        return JSONResponse(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            content={'message': 'Internal server error.'}
        )

    include_routers(app)
    return app


api = create_app()
