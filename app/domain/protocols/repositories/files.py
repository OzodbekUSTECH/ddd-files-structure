from typing import Protocol

from app.domain.entities.files import FileEntity


class IFilesRepository(Protocol):
    async def create(self, data: FileEntity) -> dict | None:
        raise NotImplementedError
