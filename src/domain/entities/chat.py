from dataclasses import dataclass

from src.domain.aggregated_roots.base import BaseAggregate
from src.domain.values.chat.chat_title import ChatTitle


@dataclass
class Chat(BaseAggregate):
    title: ChatTitle


