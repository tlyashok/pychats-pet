from dataclasses import dataclass
from enum import StrEnum
from uuid import UUID

from src.domain.exсeptions.chat.base import ChatException


class ChatMessagesExceptionType(StrEnum):
    MESSAGE_IS_NOT_FOUND = "Ошибка. Данное сообщение отсутствует в чате."


class ChatMessagesException(ChatException):
    _type: ChatMessagesExceptionType
    _chat_uuid: UUID
    _message_uuid: UUID

    def __init__(
        self,
        type_: ChatMessagesExceptionType,
        chat_uuid: UUID,
        message_uuid: UUID,
    ):
        self._type = type_
        self._chat_uuid = chat_uuid
        self._message_uuid = message_uuid

    @property
    def type_(self):
        return self._type

    @property
    def chat_uuid(self):
        return self._chat_uuid

    @property
    def message_uuid(self):
        return self._message_uuid
