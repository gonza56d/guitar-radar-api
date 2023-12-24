"""Core business exceptions."""
from abc import ABC, abstractmethod
from typing import Any


class BusinessException(ABC):

    @property
    @abstractmethod
    def message(self) -> str:
        """Exception message."""


class AlreadyExistsException(BusinessException):
    """Raised when a duplicate value has been tried to be created for certain entity."""

    def __init__(self, entity: str, field: str, value: Any):
        self._entity = entity
        self._field = field
        self._value = value

    @property
    def message(self) -> str:
        return f'{self._entity} with {self._field} {self._value} already exists.'
