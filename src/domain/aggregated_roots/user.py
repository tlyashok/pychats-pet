from dataclasses import dataclass
from uuid import UUID

from src.domain.aggregated_roots.base import BaseRoot
from src.domain.entities.user import User


@dataclass
class UserRoot(BaseRoot):
    user: User
    chats: list[UUID] #UUID чатов
