from abc import ABC, abstractmethod
from dataclasses import asdict
from typing import Type
from uuid import UUID

from pydantic import BaseModel


class ResponseModel(ABC, BaseModel):

    @classmethod
    def serialize(cls, core_output):
        return cls(**asdict(core_output))


class RequestModel(ABC, BaseModel):

    def deserialize(self, user_id: UUID | None = None):
        return self.core_model(**(self.model_dump() | ({'user_id': user_id} if user_id is not None else {})))

    @property
    @abstractmethod
    def core_model(self) -> Type:
        """Indicate core model to work with."""
