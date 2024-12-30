from src.domain.exсeptions.chat.chat_title import (
    ChatTitleException,
    ChatTitleExceptionType,
)
from src.domain.utils.constants import MAX_CHAT_TITLE_LEN
from src.domain.values.base import BaseValueObject


class ChatTitle(BaseValueObject):
    _value: str

    def __init__(self, value: str):
        self._value = value
        self._validate()

    @property
    def value(self):
        return self._value

    def __repr__(self):
        return self._value

    def _validate(self):
        if not self._value:
            raise ChatTitleException(
                type_=ChatTitleExceptionType.TITLE_IS_EMPTY,
                value=self._value,
            )
        if len(self._value) > MAX_CHAT_TITLE_LEN:
            raise ChatTitleException(
                type_=ChatTitleExceptionType.TITLE_IS_TOO_LONG,
                value=self._value,
            )
