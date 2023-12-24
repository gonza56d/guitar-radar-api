from abc import ABC, abstractmethod
from http import HTTPStatus

from app.core.exceptions import AlreadyExistsException


class APIException(ABC, Exception):

    @property
    @abstractmethod
    def status_code(self) -> HTTPStatus:
        """HTTP status code for given exception."""


class AlreadyExistsAPIException(AlreadyExistsException, APIException):

    @property
    def status_code(self) -> HTTPStatus:
        return HTTPStatus.UNPROCESSABLE_ENTITY
