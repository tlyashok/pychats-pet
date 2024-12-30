from enum import StrEnum

from src.domain.exсeptions.user.base import UserException
from src.domain.utils.constants import MAX_CHAT_TITLE_LEN


class UsernameTypesException(StrEnum):
    USERNAME_IS_EMPTY = "Ошибка. Имя пользователя не должно быть пустым."
    USERNAME_IS_TOO_LONG = (
        "Ошибка. Имя пользователя не должно превышать "
        f"{MAX_CHAT_TITLE_LEN} символов."
    )


class UsernameException(UserException):
    _type: UsernameTypesException
    _value: str

    def __init__(self, type_: UsernameTypesException, value: str):
        self._type = type_
        self._value = value

    @property
    def type_(self):
        return self._type

    @property
    def value(self):
        return self._value
