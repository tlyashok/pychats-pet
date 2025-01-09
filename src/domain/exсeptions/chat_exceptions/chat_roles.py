from enum import StrEnum

from src.domain.exсeptions.chat_exceptions.base import ChatException


class ChatRolesExceptionType(StrEnum):
    ROLE_IS_NOT_FOUND = "Ошибка. Задана несуществующая роль для пользователя."


class ChatRolesException(ChatException):
    _type: ChatRolesExceptionType
    _wrong_role: str

    def __init__(
        self,
        type_: ChatRolesExceptionType,
        wrong_role: str,
    ):
        self._type = type_
        self._wrong_role = wrong_role

    @property
    def type_(self):
        return self._type

    @property
    def wrong_role(self):
        return self._wrong_role
