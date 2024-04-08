from dataclasses import dataclass

from app.domain.entities.files import FileEntity


@dataclass
class CreateFileRequest:
    name: str
    content: bytes


@dataclass
class FileResponse:
    status: str
    url: str | None
    message: str | None

    @classmethod
    def from_entity(
        cls,
        entity: FileEntity | None = None,
        status: str = "success",
        message: str | None = None,
    ) -> "FileResponse":
        generated_url = f"http:localhost:8000/{entity.path}" if entity else None
        return cls(status=status, url=generated_url, message=message)
