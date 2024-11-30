from enum import StrEnum
from uuid import UUID

from src.domain.aggregated_roots.base import BaseRoot
from src.domain.entities.chat import Chat
from src.domain.entities.message import Message


class ChatRoles(StrEnum):
    member = "Участник"
    owner = "Владелец"

class ChatRoot(BaseRoot):
    chat: Chat
    members: dict[UUID, ChatRoles] #UUID пользователя
    messages: list[Message]

