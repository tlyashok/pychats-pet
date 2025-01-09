from uuid import UUID

from src.domain.entities.chat import Chat
from src.domain.entities.message import Message
from src.domain.events.base import DomainEvent
from src.domain.events.chat_members.user_changed_role import UserChangedRole
from src.domain.events.chat_members.user_entered_chat import UserEnteredChat
from src.domain.events.chat_members.user_left_chat import UserLeftChat
from src.domain.events.chat_messages.message_removed import MessageRemoved
from src.domain.events.chat_messages.message_sent import MessageSent
from src.domain.exсeptions.chat_exceptions.chat_members import (
    ChatMembersException,
    ChatMembersExceptionType,
)
from src.domain.exсeptions.chat_exceptions.chat_messages import (
    ChatMessagesException,
    ChatMessagesExceptionType,
)
from src.domain.utils.chat_role import ChatRole, to_chat_role


class ChatRoot:
    _chat: Chat
    _users: dict[UUID, ChatRole]  # UUID пользователя
    _messages: dict[UUID, Message]  # UUID сообщения
    _events: list[DomainEvent]

    def __init__(self, title: str, chat_uuid: UUID = None):
        self._chat = Chat(
            title=title,
            uuid=chat_uuid,
        )
        self._users = {}
        self._messages = {}
        self._events = []

    @property
    def chat(self):
        return self._chat

    @property
    def events(self):
        return self._events

    def check_user_in_chat(self, user_uuid: UUID) -> bool:
        return user_uuid in self._users

    def check_user_role(self, user_uuid: UUID) -> ChatRole:
        if user_uuid in self._users:
            return self._users[user_uuid]

        raise ChatMembersException(
            type_=ChatMembersExceptionType.USER_NOT_IN_CHAT,
            chat_uuid=self.chat.uuid,
            user_uuid=user_uuid,
        )

    def add_user(
        self,
        role: str,
        user_uuid: UUID,
    ) -> None:
        chat_role = to_chat_role(role)
        # Если пользователь уже есть в чате, вызываем исключение.
        if user_uuid in self._users:
            raise ChatMembersException(
                type_=ChatMembersExceptionType.USER_ALREADY_IN_CHAT,
                chat_uuid=self.chat.uuid,
                user_uuid=user_uuid,
            )
        self._users[user_uuid] = chat_role
        self._events.append(
            UserEnteredChat(
                user_uuid=user_uuid,
                chat_uuid=self.chat.uuid,
            ),
        )

    def remove_user(self, user_uuid: UUID) -> None:
        if user_uuid in self._users:
            self._users.pop(user_uuid)
            self._events.append(
                UserLeftChat(
                    user_uuid=user_uuid,
                    chat_uuid=self.chat.uuid,
                ),
            )
            return
        # Если пользователь не удалён, значит его нет в чате, вызываем исключение.
        raise ChatMembersException(
            type_=ChatMembersExceptionType.USER_NOT_IN_CHAT,
            chat_uuid=self.chat.uuid,
            user_uuid=user_uuid,
        )

    def set_user_role(self, user_uuid: UUID, role: str) -> None:
        chat_role = to_chat_role(role)
        if user_uuid in self._users:
            self._users[user_uuid] = chat_role
            self._events.append(
                UserChangedRole(
                    user_uuid=user_uuid,
                    chat_uuid=self.chat.uuid,
                    new_role=chat_role,
                ),
            )
            return
        raise ChatMembersException(
            type_=ChatMembersExceptionType.USER_NOT_IN_CHAT,
            chat_uuid=self.chat.uuid,
            user_uuid=user_uuid,
        )

    def add_message(self, user_uuid: UUID, message: str) -> None:
        message = Message(
            message_text=message,
            user_uuid=user_uuid,
        )
        self._messages[message.uuid] = message
        self._events.append(
            MessageSent(
                message_uuid=message.uuid,
                chat_uuid=self.chat.uuid,
            ),
        )

    def remove_message(self, message_uuid: UUID) -> None:
        if message_uuid in self._messages:
            self._messages.pop(message_uuid)
            self._events.append(
                MessageRemoved(
                    message_uuid=message_uuid,
                    chat_uuid=self.chat.uuid,
                ),
            )
            return
        raise ChatMessagesException(
            type_=ChatMessagesExceptionType.MESSAGE_IS_NOT_FOUND,
            chat_uuid=self.chat.uuid,
            message_uuid=message_uuid,
        )

    def get_all_messages(self) -> list[Message]:
        return list(self._messages.values())

    def get_all_users_uuid(self) -> list[UUID]:
        return list(self._users.keys())

    def get_all_users_with_roles(self) -> dict[UUID, ChatRole]:
        return self._users
