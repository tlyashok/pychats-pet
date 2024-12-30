from datetime import datetime
from uuid import UUID

from src.domain.entities.base import BaseEntity
from src.domain.values.chat.message_text import MessageText


class Message(BaseEntity):
    _created_at: datetime
    _user_uuid: UUID
    _message_text: MessageText

    def __init__(self, user_uuid: UUID, message_text: str, uuid: UUID = None):
        super().__init__(uuid)
        self._created_at = datetime.now()
        self._user_uuid = user_uuid
        self._message_text = MessageText(message_text)

    @property
    def created_at(self):
        return self._created_at

    @property
    def user_uuid(self):
        return self._user_uuid

    @property
    def message_text(self):
        return self._message_text.value
