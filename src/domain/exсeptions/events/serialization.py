from enum import StrEnum

from src.domain.exсeptions.events.base import EventException


class EventSerializationTypesException(StrEnum):
    DictionaryIsImproperlyStructured = "Ошибка. Словарь имеет некорректную структуру."


class EventSerializationException(EventException):
    _type: EventSerializationTypesException
    _value: dict

    def __init__(self, type_: EventSerializationTypesException, value: dict):
        self._type = type_
        self._value = value

    @property
    def type_(self):
        return self._type

    @property
    def value(self):
        return self._value
