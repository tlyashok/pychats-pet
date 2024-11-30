from dataclasses import dataclass
from enum import StrEnum

from src.domain.constants import MAX_CHAT_TITLE_LEN
from src.domain.exсeptions.chat.base import ChatException


class ChatTitleTypesException(StrEnum):
    TITLE_IS_EMPTY = "Ошибка. Название чата не должно быть пустым."
    TITLE_IS_TOO_LONG = ("Ошибка. Название чата не должно превышать "
                     f"{MAX_CHAT_TITLE_LEN} символов.")

@dataclass(frozen=True)
class ChatTitleException(ChatException):
    type: ChatTitleTypesException
