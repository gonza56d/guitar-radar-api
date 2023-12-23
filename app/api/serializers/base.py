from abc import ABC, abstractmethod
from dataclasses import asdict
from typing import Type

from pydantic import BaseModel


class ResponseModel(ABC, BaseModel):

    @classmethod
    def serialize(cls, core_output):
        return cls(**asdict(core_output))


class RequestModel(ABC, BaseModel):

    def deserialize(self):
        return self.core_model(**self.model_dump())

    @property
    @abstractmethod
    def core_model(self) -> Type:
        """Indicate core model to work with."""
