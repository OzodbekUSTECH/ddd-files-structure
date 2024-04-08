from uuid6 import uuid6

from app.application.dto import files as files_dto
from app.domain.entities.files import FileEntity
from app.domain.protocols import repositories as interface_repos


class FilesService:

    def __init__(
        self,
        uow: interface_repos.IUnitOfWork,
        files_repository: interface_repos.IFilesRepository,
    ) -> None:
        self.uow = uow
        self.files_repository = files_repository

    async def create_files(
        self, data: list[files_dto.CreateFileRequest]
    ) -> dict[int | str, files_dto.FileResponse]:
        response = {}
        for idx, file in enumerate(data):

            try:
                secured_name = f"{uuid6()}.{file.name}"
                file_entity = FileEntity.create(name=secured_name)
                await self.files_repository.create(data=file_entity)

                with open(f"./{file_entity.path}", "wb") as f:
                    f.write(file.content)
                f.close()

                response[idx] = files_dto.FileResponse.from_entity(entity=file_entity)
            except Exception as msg:
                response[idx] = files_dto.FileResponse.from_entity(
                    status="failed", message=str(msg)
                )

        return response
