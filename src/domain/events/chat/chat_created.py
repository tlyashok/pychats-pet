from datetime import datetime
from uuid import UUID

from src.domain.events.base import DomainEvent, DomainEventType
from src.domain.exсeptions.events.serialization import (
    EventSerializationException,
    EventSerializationTypesException,
)


class ChatCreated(DomainEvent):
    _user_uuid: UUID
    _chat_uuid: UUID

    def __init__(
        self,
        user_uuid: UUID,
        chat_uuid: UUID,
        uuid: UUID = None,
        created_at: datetime = None,
    ):
        super().__init__(uuid, created_at, DomainEventType.CHAT_CREATED)
        self._user_uuid = user_uuid
        self._chat_uuid = chat_uuid

    @property
    def user_uuid(self):
        return self._user_uuid

    @property
    def chat_uuid(self):
        return self._chat_uuid

    @staticmethod
    def from_dict_factory(data: dict):
        if "user_uuid" not in data or "chat_uuid" not in data:
            raise EventSerializationException(
                type_=EventSerializationTypesException.DictionaryIsImproperlyStructured,
                value=data,
            )

        return ChatCreated(
            user_uuid=data["user_uuid"],
            chat_uuid=data["chat_uuid"],
            uuid=data.get("uuid"),
            created_at=data.get("created_at"),
        )

    def to_dict(self):
        dict_ = super().to_dict()
        dict_["user_uuid"] = str(self._user_uuid)
        dict_["chat_uuid"] = str(self._chat_uuid)
