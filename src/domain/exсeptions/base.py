from dataclasses import dataclass


@dataclass(frozen=True)
class ApplicationException(Exception):
    type: str
    error_value: str
