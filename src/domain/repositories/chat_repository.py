from abc import ABC, abstractmethod
from src.domain.aggregated_roots.chat_root import ChatRoot


class ChatRepository(ABC):
    @abstractmethod
    def save(self, chat_root: ChatRoot) -> None:
        pass

    @abstractmethod
    def get(self, chat_uuid) -> ChatRoot:
        pass
