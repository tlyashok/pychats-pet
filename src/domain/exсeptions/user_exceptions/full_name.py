from enum import StrEnum

from src.domain.exсeptions.user_exceptions.base import UserException
from src.domain.utils.constants import MAX_FULLNAME_LEN


class UserFullnameTypesException(StrEnum):
    USER_FULLNAME_IS_EMPTY = "Ошибка. Полное имя не должно быть пустым."
    USER_FULLNAME_IS_TOO_LONG = (
        "Ошибка. Полное имя не должно превышать " f"{MAX_FULLNAME_LEN} символов."
    )


class UserFullnameException(UserException):
    _type: UserFullnameTypesException
    _value: str

    def __init__(self, type_: UserFullnameTypesException, value: str):
        self._type = type_
        self._value = value

    @property
    def type_(self):
        return self._type

    @property
    def value(self):
        return self._value
