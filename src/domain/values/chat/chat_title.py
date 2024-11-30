from dataclasses import dataclass

from src.domain.constants import MAX_CHAT_TITLE_LEN
from src.domain.exсeptions.chat.chat_title import (
    ChatTitleException,
    ChatTitleTypesException,
)
from src.domain.values.base import BaseValueObject


@dataclass(frozen=True)
class ChatTitle(BaseValueObject):
    value: str

    def _validate(self):
        if not self.value:
            raise ChatTitleException(ChatTitleTypesException.TITLE_IS_EMPTY,
                                     self.value)
        if len(self.value) > MAX_CHAT_TITLE_LEN:
            raise ChatTitleException(ChatTitleTypesException.TITLE_IS_TOO_LONG,
                                     self.value)
