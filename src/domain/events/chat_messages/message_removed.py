from datetime import datetime
from uuid import UUID

from src.domain.events.base import DomainEvent, DomainEventType
from src.domain.exсeptions.events.serialization import (
    EventSerializationException,
    EventSerializationTypesException,
)


class MessageRemoved(DomainEvent):
    _message_uuid: UUID
    _chat_uuid: UUID

    def __init__(
        self,
        message_uuid: UUID,
        chat_uuid: UUID,
        uuid: UUID = None,
        created_at: datetime = None,
    ):
        super().__init__(uuid, created_at, DomainEventType.MESSAGE_REMOVED)
        self._message_uuid = message_uuid
        self._chat_uuid = chat_uuid

    @property
    def message_uuid(self):
        return self._message_uuid

    @property
    def chat_uuid(self):
        return self._chat_uuid

    @staticmethod
    def from_dict_factory(data: dict):
        if "message_uuid" not in data or "chat_uuid" not in data:
            raise EventSerializationException(
                type_=EventSerializationTypesException.DictionaryIsImproperlyStructured,
                value=data,
            )

        return MessageRemoved(
            message_uuid=data["message_uuid"],
            chat_uuid=data["chat_uuid"],
            uuid=data.get("uuid"),
            created_at=data.get("created_at"),
        )

    def to_dict(self):
        dict_ = super().to_dict()
        dict_["message_uuid"] = str(self._message_uuid)
        dict_["chat_uuid"] = str(self._chat_uuid)
