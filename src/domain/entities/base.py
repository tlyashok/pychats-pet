from abc import ABC
from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class BaseEntity(ABC):
    uid: UUID = field(
        default_factory=uuid4,
        kw_only=True,
    )

    def __hash__(self) -> int:
        return hash(self.uid)

    def __eq__(self, other: "BaseEntity") -> bool:
        return self.uid == other.uid
