from dataclasses import dataclass

from src.domain.entities.base import BaseEntity
from src.domain.values.user.full_name import Fullname
from src.domain.values.user.username import Username


@dataclass
class User(BaseEntity):
    username: Username
    full_name: Fullname
