from dataclasses import dataclass
from enum import StrEnum

from src.domain.constants import MAX_FULLNAME_LEN
from src.domain.exсeptions.user.base import UserException


class UserFullnameTypesException(StrEnum):
    USER_FULLNAME_IS_EMPTY = "Ошибка. Полное имя не должно быть пустым."
    USER_FULLNAME_IS_TOO_LONG = ("Ошибка. Полное имя не должно превышать "
                     f"{MAX_FULLNAME_LEN} символов.")

@dataclass(frozen=True)
class UserFullnameException(UserException):
    type: UserFullnameTypesException
