from abc import ABC, abstractmethod
from http import HTTPStatus

from app.core.exceptions import AlreadyExistsException, NotFoundException, UnauthorizedException


class APIException(ABC, Exception):

    @property
    @abstractmethod
    def status_code(self) -> HTTPStatus:
        """HTTP status code for given exception."""


class AlreadyExistsAPIException(AlreadyExistsException, APIException):

    @property
    def status_code(self) -> HTTPStatus:
        return HTTPStatus.UNPROCESSABLE_ENTITY


class NotFoundAPIException(NotFoundException, APIException):

    @property
    def status_code(self) -> HTTPStatus:
        return HTTPStatus.NOT_FOUND


class UnauthorizedAPIException(UnauthorizedException, APIException):

    @property
    def status_code(self) -> HTTPStatus:
        return HTTPStatus.UNAUTHORIZED
