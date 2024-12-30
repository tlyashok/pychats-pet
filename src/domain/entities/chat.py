from uuid import UUID

from src.domain.entities.base import BaseEntity
from src.domain.values.chat.chat_title import ChatTitle


class Chat(BaseEntity):
    _title: ChatTitle

    def __init__(self, title: str, uuid: UUID = None):
        super().__init__(uuid)
        self._title = ChatTitle(title)

    @property
    def title(self):
        return self._title

    def to_dict(self):
        dict_ = super().to_dict()
        dict_["title"] = str(self._title)
