from dataclasses import dataclass
from enum import StrEnum

from src.domain.constants import MAX_CHAT_MESSAGE_LEN
from src.domain.exсeptions.chat.base import ChatException


class MessageTextTypesException(StrEnum):
    MESSAGE_IS_EMPTY = "Ошибка. Сообщение не должно быть пустым."
    MESSAGE_IS_TOO_LONG = ("Ошибка. Сообщение не должно превышать "
                       f"{MAX_CHAT_MESSAGE_LEN} символов.")

@dataclass(frozen=True)
class MessageTextException(ChatException):
    type: MessageTextTypesException
