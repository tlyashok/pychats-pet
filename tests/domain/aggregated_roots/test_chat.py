from uuid import uuid4

import pytest
from src.domain.aggregated_roots.chat_root import ChatRoot
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
from src.domain.exсeptions.chat_exceptions.chat_roles import (
    ChatRolesException,
    ChatRolesExceptionType,
)
from src.domain.utils.chat_role import ChatRole, to_chat_role


@pytest.fixture
def chat_root():
    return ChatRoot(title="Test Chat", chat_uuid=uuid4())


def test_add_user_success(chat_root):
    user_uuid = uuid4()
    chat_root.add_user(role="MEMBER", user_uuid=user_uuid)

    assert user_uuid in chat_root.get_all_users_uuid()
    assert chat_root.get_all_users_with_roles()[user_uuid] == ChatRole.MEMBER
    assert len(chat_root.events) == 1
    assert isinstance(chat_root.events[0], UserEnteredChat)


def test_add_user_already_in_chat(chat_root):
    user_uuid = uuid4()
    chat_root.add_user(role="MEMBER", user_uuid=user_uuid)

    with pytest.raises(ChatMembersException) as exception:
        chat_root.add_user(role="MEMBER", user_uuid=user_uuid)

    assert exception.value.type_ == ChatMembersExceptionType.USER_ALREADY_IN_CHAT
    assert exception.value.chat_uuid == chat_root.chat.uuid
    assert exception.value.user_uuid == user_uuid


def test_remove_user_success(chat_root):
    user_uuid = uuid4()
    chat_root.add_user(role="MEMBER", user_uuid=user_uuid)
    chat_root.remove_user(user_uuid)

    assert user_uuid not in chat_root.get_all_users_uuid()
    assert len(chat_root.events) == 2
    assert isinstance(chat_root.events[1], UserLeftChat)


def test_remove_user_not_in_chat(chat_root):
    user_uuid = uuid4()

    with pytest.raises(ChatMembersException) as exception:
        chat_root.remove_user(user_uuid)

    assert exception.value.type_ == ChatMembersExceptionType.USER_NOT_IN_CHAT
    assert exception.value.chat_uuid == chat_root.chat.uuid
    assert exception.value.user_uuid == user_uuid


def test_set_user_role_success(chat_root):
    user_uuid = uuid4()
    chat_root.add_user(role="MEMBER", user_uuid=user_uuid)
    chat_root.set_user_role(user_uuid, "OWNER")

    assert chat_root.get_all_users_with_roles()[user_uuid] == ChatRole.OWNER
    assert len(chat_root.events) == 2
    assert isinstance(chat_root.events[1], UserChangedRole)


def test_set_user_role_not_in_chat(chat_root):
    user_uuid = uuid4()

    with pytest.raises(ChatMembersException) as exception:
        chat_root.set_user_role(user_uuid, "OWNER")

    assert exception.value.type_ == ChatMembersExceptionType.USER_NOT_IN_CHAT
    assert exception.value.chat_uuid == chat_root.chat.uuid
    assert exception.value.user_uuid == user_uuid


def test_to_chat_role_invalid_role():
    with pytest.raises(ChatRolesException) as exception:
        to_chat_role("INVALID_ROLE")

    assert exception.value.type_ == ChatRolesExceptionType.ROLE_IS_NOT_FOUND
    assert exception.value.wrong_role == "INVALID_ROLE"


def test_add_message_success(chat_root):
    user_uuid = uuid4()
    message_text = "Hello, World!"
    chat_root.add_user(role="MEMBER", user_uuid=user_uuid)
    assert len(chat_root.events) == 1
    chat_root.add_message(user_uuid=user_uuid, message=message_text)
    assert len(chat_root.events) == 2
    messages = chat_root.get_all_messages()
    assert len(messages) == 1
    assert messages[0].message_text == message_text
    assert isinstance(chat_root.events[0], UserEnteredChat)
    assert isinstance(chat_root.events[1], MessageSent)


def test_remove_message_success(chat_root):
    user_uuid = uuid4()
    message_text = "Message to be removed"
    chat_root.add_user(role="MEMBER", user_uuid=user_uuid)
    chat_root.add_message(user_uuid=user_uuid, message=message_text)

    message_uuid = list(chat_root._messages.keys())[0]
    chat_root.remove_message(message_uuid)

    assert message_uuid not in chat_root._messages
    assert len(chat_root.events) == 3
    assert isinstance(chat_root.events[2], MessageRemoved)


def test_remove_message_not_found(chat_root):
    with pytest.raises(ChatMessagesException) as exception:
        chat_root.remove_message(uuid4())

    assert exception.value.type_ == ChatMessagesExceptionType.MESSAGE_IS_NOT_FOUND
    assert exception.value.chat_uuid == chat_root.chat.uuid
    assert exception.value.message_uuid is not None
