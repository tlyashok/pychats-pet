from uuid import UUID

from src.domain.aggregated_roots.base import BaseRoot
from src.domain.entities.user import User


class UserRoot(BaseRoot):
    _user: User

    def __init__(self, username: str, full_name: str, user_uuid: UUID = None) -> None:
        self._user = User(
            username=username,
            full_name=full_name,
            uuid=user_uuid,
        )

    @property
    def user(self) -> User:
        return self._user
