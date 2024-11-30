from datetime import datetime

import pytest
from src.domain.entities.message import Chat, Message
from src.domain.exсeptions.messages import TitleTooLongException
from src.domain.values.messages import Text, Title


def test_create_message_success():
    text = Text("a" * 255)
    message = Message(text)

    assert message.text == text
    assert message.created_at.date() == datetime.today().date()


def test_comparing_messages():
    text = Text("a" * 255)
    message1 = Message(text)
    message2 = Message(text)

    assert message1 != message2


def test_create_chat_with_normal_title_length():
    title = Title("a" * 255)
    chat = Chat(title)

    assert chat.title == title
    assert chat.created_at.date() == datetime.today().date()


def test_create_chat_with_too_long_title():
    with pytest.raises(TitleTooLongException):
        title = Title("a" * 256)
        Chat(title)
