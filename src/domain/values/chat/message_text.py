from dataclasses import dataclass

from src.domain.constants import MAX_CHAT_MESSAGE_LEN
from src.domain.exсeptions.chat.message_text import (
    MessageTextException,
    MessageTextTypesException,
)
from src.domain.values.base import BaseValueObject


@dataclass(frozen=True)
class MessageText(BaseValueObject):
    value: str

    def _validate(self):
        if not self.value:
            raise MessageTextException(
                MessageTextTypesException.MESSAGE_IS_EMPTY, self.value,
            )
        if len(self.value) > MAX_CHAT_MESSAGE_LEN:
            raise MessageTextException(
                MessageTextTypesException.MESSAGE_IS_TOO_LONG, self.value,
            )
