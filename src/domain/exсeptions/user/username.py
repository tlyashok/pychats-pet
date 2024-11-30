from dataclasses import dataclass
from enum import StrEnum

from src.domain.constants import MAX_CHAT_TITLE_LEN
from src.domain.exсeptions.user.base import UserException


class UsernameTypesException(StrEnum):
    USERNAME_IS_EMPTY = "Ошибка. Имя пользователя не должно быть пустым."
    USERNAME_IS_TOO_LONG = ("Ошибка. Имя пользователя не должно превышать "
                     f"{MAX_CHAT_TITLE_LEN} символов.")

@dataclass(frozen=True)
class UsernameException(UserException):
    type: UsernameTypesException
