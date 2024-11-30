from dataclasses import dataclass

from src.domain.exсeptions.base import ApplicationException


@dataclass(frozen=True)
class UserException(ApplicationException):
    ...
