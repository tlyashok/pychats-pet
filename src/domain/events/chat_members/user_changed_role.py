from datetime import datetime
from uuid import UUID

from src.domain.events.base import DomainEvent, DomainEventType
from src.domain.exсeptions.events_exceptions.serialization import (
    EventSerializationException,
    EventSerializationTypesException,
)
from src.domain.utils.chat_role import ChatRole


class UserChangedRole(DomainEvent):
    _user_uuid: UUID
    _chat_uuid: UUID
    _new_role: ChatRole

    def __init__(
        self,
        user_uuid: UUID,
        chat_uuid: UUID,
        new_role: ChatRole,
        uuid: UUID = None,
        created_at: datetime = None,
    ):
        super().__init__(uuid, created_at, DomainEventType.USER_CHANGED_ROLE)
        self._user_uuid = user_uuid
        self._chat_uuid = chat_uuid
        self._new_role = new_role

    @property
    def user_uuid(self):
        return self._user_uuid

    @property
    def chat_uuid(self):
        return self._chat_uuid

    @property
    def new_role(self):
        return self._new_role

    @staticmethod
    def from_dict_factory(data: dict):
        if "user_uuid" not in data or "chat_uuid" not in data or "new_role" not in data:
            raise EventSerializationException(
                type_=EventSerializationTypesException.DictionaryIsImproperlyStructured,
                value=data,
            )

        return UserChangedRole(
            user_uuid=data["user_uuid"],
            chat_uuid=data["chat_uuid"],
            new_role=data["new_role"],
            uuid=data.get("uuid"),
            created_at=data.get("created_at"),
        )

    def to_dict(self):
        dict_ = super().to_dict()
        dict_["user_uuid"] = str(self._user_uuid)
        dict_["chat_uuid"] = str(self._chat_uuid)
        dict_["new_role"] = str(self._new_role)
