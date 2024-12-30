from src.domain.exсeptions.user.full_name import (
    UserFullnameException,
    UserFullnameTypesException,
)
from src.domain.utils.constants import MAX_USERNAME_LEN
from src.domain.values.base import BaseValueObject


class FullName(BaseValueObject):
    _value: str

    def __init__(self, value: str):
        self._value = value
        self._validate()

    @property
    def value(self):
        return self._value

    def _validate(self):
        if not self._value:
            raise UserFullnameException(
                type_=UserFullnameTypesException.USER_FULLNAME_IS_EMPTY,
                value=self._value,
            )
        if len(self._value) > MAX_USERNAME_LEN:
            raise UserFullnameException(
                type_=UserFullnameTypesException.USER_FULLNAME_IS_TOO_LONG,
                value=self._value,
            )
