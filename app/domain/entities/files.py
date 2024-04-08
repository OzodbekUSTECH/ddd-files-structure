from dataclasses import dataclass
from uuid import uuid4

from app.domain.value_objects.id import IdVO


@dataclass(frozen=True)
class FileEntity:
    id: IdVO
    name: str
    path: str

    @classmethod
    def create(cls, name: str) -> "FileEntity":
        return cls(id=IdVO(uuid4()), name=name, path=f"app/media/files/{name}")
