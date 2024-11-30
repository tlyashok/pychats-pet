from dataclasses import dataclass

from src.domain.constants import MAX_USERNAME_LEN
from src.domain.exсeptions.user.username import (
    UsernameException,
    UsernameTypesException,
)
from src.domain.values.base import BaseValueObject


@dataclass(frozen=True)
class Username(BaseValueObject):
    value: str

    def _validate(self):
        if not self.value:
            raise UsernameException(UsernameTypesException.USERNAME_IS_EMPTY,
                                     self.value)
        if len(self.value) > MAX_USERNAME_LEN:
            raise UsernameException(UsernameTypesException.USERNAME_IS_TOO_LONG,
                                     self.value)
