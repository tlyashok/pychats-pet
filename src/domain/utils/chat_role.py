from enum import StrEnum

from src.domain.exсeptions.chat.chat_roles import (
    ChatRolesException,
    ChatRolesExceptionType,
)


class ChatRole(StrEnum):
    MEMBER = "MEMBER"
    OWNER = "OWNER"


def to_chat_role(role: str) -> ChatRole:
    try:
        # Пытаемся преобразовать строку role к StrEnum, иначе получаем ValueError.
        role = ChatRole(role)
        return role
    except ValueError:
        raise ChatRolesException(
            type_=ChatRolesExceptionType.ROLE_IS_NOT_FOUND,
            wrong_role=role,
        )
