from enum import StrEnum

from src.domain.exсeptions.chat_exceptions.base import ChatException
from src.domain.utils.constants import MAX_CHAT_MESSAGE_LEN


class MessageTextExceptionType(StrEnum):
    MESSAGE_IS_EMPTY = "Ошибка. Сообщение не должно быть пустым."
    MESSAGE_IS_TOO_LONG = (
        "Ошибка. Сообщение не должно превышать " f"{MAX_CHAT_MESSAGE_LEN} символов."
    )


class MessageTextException(ChatException):
    _type: MessageTextExceptionType
    _value: str

    def __init__(self, type_: MessageTextExceptionType, value: str):
        self._type = type_
        self._value = value

    @property
    def type_(self):
        return self._type

    @property
    def value(self):
        return self._value
