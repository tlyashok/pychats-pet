from dataclasses import dataclass

from domain.values.message import Text

@dataclass
class Message:
    uid: str
    text: Text

