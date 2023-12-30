from http import HTTPStatus
from typing import Type

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.api.exceptions import APIException, UnauthorizedAPIException
from app.containers import Container
from app.api.routers.auth import router as auth_router
from app.api.routers.brands import router as brand_router
from app.api.routers.components import router as components_router
from app.api.routers.health import router as health_router
from app.core.exceptions import BusinessException, UnauthorizedException

core_exception_map: dict[Type[BusinessException], APIException] = {
    UnauthorizedException: UnauthorizedAPIException()
}


def include_routers(app: FastAPI) -> None:
    app.include_router(auth_router)
    app.include_router(brand_router)
    app.include_router(components_router)
    app.include_router(health_router)


def create_app() -> FastAPI:
    container = Container()
    app = FastAPI()
    app.container = container

    @app.middleware('http')
    async def api_exception_handler(request: Request, call_next):
        try:
            return await call_next(request)
        except (BusinessException, APIException) as exc:
            if not isinstance(exc, APIException):
                exc = core_exception_map[type(exc)]
            return JSONResponse(
                status_code=exc.status_code,
                content={'message': exc.message}
            )
        except Exception:
            return JSONResponse(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                content={'message': 'Internal server error.'}
            )

    include_routers(app)
    return app


api = create_app()
