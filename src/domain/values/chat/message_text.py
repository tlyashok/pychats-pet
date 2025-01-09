from src.domain.exсeptions.chat_exceptions.message_text import (
    MessageTextException,
    MessageTextExceptionType,
)
from src.domain.utils.constants import MAX_CHAT_MESSAGE_LEN
from src.domain.values.base import BaseValueObject


class MessageText(BaseValueObject):
    _value: str

    def __init__(self, value: str):
        self._value = value
        self._validate()

    @property
    def value(self):
        return self._value

    def _validate(self):
        if not self._value:
            raise MessageTextException(
                type_=MessageTextExceptionType.MESSAGE_IS_EMPTY,
                value=self._value,
            )
        if len(self._value) > MAX_CHAT_MESSAGE_LEN:
            raise MessageTextException(
                type_=MessageTextExceptionType.MESSAGE_IS_TOO_LONG,
                value=self._value,
            )
