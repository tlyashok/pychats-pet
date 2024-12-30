from enum import StrEnum
from uuid import UUID

from src.domain.exсeptions.chat.base import ChatException


class ChatMembersExceptionType(StrEnum):
    USER_NOT_IN_CHAT = "Ошибка. Данный пользователь отсутствует в чате."
    USER_ALREADY_IN_CHAT = "Ошибка. Пользователь уже состоит в этом чате."
    ACCESS_DENIED = "Ошибка. Пользователь не имеет права на данное действие."


class ChatMembersException(ChatException):
    _type: ChatMembersExceptionType
    _chat_uuid: UUID
    _user_uuid: UUID

    def __init__(
        self,
        type_: ChatMembersExceptionType,
        chat_uuid: UUID,
        user_uuid: UUID,
    ):
        self._type = type_
        self._chat_uuid = chat_uuid
        self._user_uuid = user_uuid

    @property
    def type_(self):
        return self._type

    @property
    def chat_uuid(self):
        return self._chat_uuid

    @property
    def user_uuid(self):
        return self._user_uuid
