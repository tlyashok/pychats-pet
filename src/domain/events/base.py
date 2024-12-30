import json
from abc import ABC
from datetime import UTC, datetime
from enum import StrEnum
from uuid import UUID, uuid4


class DomainEventType(StrEnum):
    MESSAGE_SENT = "MESSAGE_SENT"
    MESSAGE_REMOVED = "MESSAGE_REMOVED"
    USER_ENTERED_CHAT = "USER_HAS_ENTERED_CHAT"
    USER_LEFT_CHAT = "USER_HAS_LEFT_CHAT"
    USER_CHANGED_ROLE = "USER_CHANGED_ROLE"
    CHAT_CREATED = "CHAT_CREATED"


class DomainEvent(ABC):
    _uuid: UUID
    _created_at: datetime
    _type: DomainEventType

    def __init__(
        self,
        uuid: UUID = None,
        created_at: datetime = None,
        type_: DomainEventType = None,
    ):
        self._uuid = uuid
        self._created_at = created_at
        self._type = type_

        if self._uuid is None:
            self._uuid = uuid4()

        if self._created_at is None:
            self._created_at = datetime.now(UTC)

    @property
    def uuid(self):
        return self._uuid

    @property
    def created_at(self):
        return self._created_at

    @property
    def type(self):
        return self._type

    @staticmethod
    def from_dict_factory(data: dict):
        return DomainEvent(
            uuid=data.get("uuid"),
            created_at=data.get("created_at"),
            type_=data.get("type"),
        )

    def to_json(self) -> str:
        prepared_obj = self.to_dict()
        return json.dumps(prepared_obj)

    def to_dict(self) -> dict:
        return {
            "uuid": str(self._uuid),
            "created_at": str(self._created_at),
            "type": self._type,
        }
