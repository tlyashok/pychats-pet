from uuid import UUID

from src.domain.entities.base import BaseEntity
from src.domain.values.user.full_name import FullName
from src.domain.values.user.username import Username


class User(BaseEntity):
    _username: Username
    _full_name: FullName

    def __init__(self, username: str, full_name: str, uuid: UUID = None):
        super().__init__(uuid)
        self._username = Username(username)
        self._full_name = FullName(full_name)

    @property
    def username(self):
        return self._username

    @property
    def full_name(self):
        return self._full_name
