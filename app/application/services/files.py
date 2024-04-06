from app.domain.protocols.uow import IUnitOfWork
from app.domain.protocols.repositories.files import IFilesRepository
from app.application.dto import files as files_dto
from app.domain.entities.files import FileEntity


class FilesService:

    def __init__(
            self,
            uow: IUnitOfWork,
            files_repository: IFilesRepository
    ) -> None:
        self.uow = uow
        self.files_repository = files_repository

    async def create_file(self, data: files_dto.CreateFileRequest) -> files_dto.FileResponse:
        data = FileEntity.create(
            name=data.name,
            path=data.path
        )
        await self.files_repository.create(data)
        await self.uow.commit()
        return files_dto.FileResponse.from_entity(data)