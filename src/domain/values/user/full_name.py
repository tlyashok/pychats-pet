from dataclasses import dataclass

from src.domain.constants import MAX_USERNAME_LEN
from src.domain.exсeptions.user.full_name import (
    UserFullnameException,
    UserFullnameTypesException,
)
from src.domain.values.base import BaseValueObject


@dataclass(frozen=True)
class Fullname(BaseValueObject):
    value: str

    def _validate(self):
        if not self.value:
            raise UserFullnameException(
                UserFullnameTypesException.USER_FULLNAME_IS_EMPTY,
                self.value,
            )
        if len(self.value) > MAX_USERNAME_LEN:
            raise UserFullnameException(
                UserFullnameTypesException.USER_FULLNAME_IS_TOO_LONG,
                self.value,
            )
