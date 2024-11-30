from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID

from src.domain.entities.base import BaseEntity
from src.domain.values.chat.message_text import MessageText


@dataclass
class Message(BaseEntity):
    created_at: datetime = field(
        default_factory=datetime.now,
        kw_only=True,
    )
    user: UUID
    message_text: MessageText
