from abc import ABC, abstractmethod
from uuid import UUID
from src.domain.aggregated_roots.user_root import UserRoot


class UserRepository(ABC):
    @abstractmethod
    def save(self, user_root: UserRoot) -> None:
        pass

    @abstractmethod
    def get(self, user_uuid: UUID) -> UserRoot:
        pass

    @abstractmethod
    def get_by_username(self, username: str) -> UserRoot:
        pass

    @abstractmethod
    def remove(self, user_uuid: UUID) -> None:
        pass
