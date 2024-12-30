from uuid import UUID, uuid4


class BaseEntity:
    _uuid: UUID

    def __init__(self, uuid=None):
        if uuid is None:
            self._uuid = uuid4()
        else:
            self._uuid = uuid

    def __str__(self):
        return str(self._uuid)

    @property
    def uuid(self):
        return self._uuid

    def to_dict(self):
        return {
            "uuid": str(self._uuid),
        }

    def __hash__(self) -> int:
        return hash(self.uuid)

    def __eq__(self, other: "BaseEntity") -> bool:
        return self.uuid == other.uuid
