from uuid import UUID

from src.domain.aggregated_roots.chat_root import ChatRoot
from src.application.dto.chat_dto import ChatDTO, MessageDTO

from src.domain.repositories.chat_repository import ChatRepository


class ChatService:
    def __init__(self, chat_repository: ChatRepository):
        self.chat_repository = chat_repository

    def create_chat(self, title: str) -> ChatDTO:
        """Создаёт новый чат."""
        chat_root = ChatRoot(title=title)
        self.chat_repository.save(chat_root)
        return ChatDTO.from_domain(chat_root.chat)

    def add_user_to_chat(self, chat_uuid: UUID, user_uuid: UUID, role: str) -> None:
        """Добавляет пользователя в чат."""
        chat_root = self.chat_repository.get(chat_uuid)
        chat_root.add_user(role=role, user_uuid=user_uuid)
        self.chat_repository.save(chat_root)

    def remove_user_from_chat(self, chat_uuid: UUID, user_uuid: UUID) -> None:
        """Удаляет пользователя из чата."""
        chat_root = self.chat_repository.get(chat_uuid)
        chat_root.remove_user(user_uuid=user_uuid)
        self.chat_repository.save(chat_root)

    def send_message(self, chat_uuid: UUID, user_uuid: UUID, message: str) -> MessageDTO:
        """Отправляет сообщение в чат."""
        chat_root = self.chat_repository.get(chat_uuid)
        chat_root.add_message(user_uuid=user_uuid, message=message)
        self.chat_repository.save(chat_root)

        last_event = chat_root.events[-1]
        return MessageDTO.from_event(last_event)

    def get_chat_messages(self, chat_uuid: UUID) -> list[MessageDTO]:
        """Возвращает все сообщения чата."""
        chat_root = self.chat_repository.get(chat_uuid)
        messages = chat_root.get_all_messages()
        return [MessageDTO.from_domain(msg) for msg in messages]

    def get_chat_users(self, chat_uuid: UUID) -> dict[UUID, str]:
        """Возвращает всех пользователей чата с их ролями."""
        chat_root = self.chat_repository.get(chat_uuid)
        return {user_uuid: role.value for user_uuid, role in chat_root.get_all_users_with_roles().items()}
