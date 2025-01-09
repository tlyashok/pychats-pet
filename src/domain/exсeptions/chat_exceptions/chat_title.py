from enum import StrEnum

from src.domain.exсeptions.chat_exceptions.base import ChatException
from src.domain.utils.constants import MAX_CHAT_TITLE_LEN


class ChatTitleExceptionType(StrEnum):
    TITLE_IS_EMPTY = "Ошибка. Название чата не должно быть пустым."
    TITLE_IS_TOO_LONG = (
        "Ошибка. Название чата не должно превышать " f"{MAX_CHAT_TITLE_LEN} символов."
    )


class ChatTitleException(ChatException):
    _type: ChatTitleExceptionType
    _value: str

    def __init__(self, type_: ChatTitleExceptionType, value: str):
        self._type = type_
        self._value = value

    @property
    def type_(self):
        return self._type

    @property
    def value(self):
        return self._value
