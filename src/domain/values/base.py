from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class BaseValueObject(ABC):
    def __post_init__(self):
        self._validate()

    @abstractmethod
    def _validate(self): ...
