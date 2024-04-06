from dataclasses import dataclass
from uuid import UUID
from app.domain.entities.files import FileEntity


@dataclass
class CreateFileRequest:
    name: str
    path: str


@dataclass
class UpdateFileRequest:
    name: str
    path: str


@dataclass
class FileResponse:
    id: UUID
    name: str
    path: str

    @classmethod
    def from_entity(cls, entity: FileEntity) -> "FileResponse":
        return cls(
            id=entity.id.value,
            name=entity.name,
            path=entity.path
        )
