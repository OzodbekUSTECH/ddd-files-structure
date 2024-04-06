from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.protocols.repositories.files import IFilesRepository
from app.domain.entities.files import FileEntity
from sqlalchemy import insert
from app.infrastucture.db import models


class SqlalchemyFilesRepository(IFilesRepository):
    __slots__ = ("session",)

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, data: FileEntity) -> None:
        stmt = insert(models.File).values(
            id=data.id.value,
            name=data.name,
            path=data.path
        )
        await self.session.execute(stmt)
