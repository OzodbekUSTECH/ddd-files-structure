from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter, UploadFile

from app.application.dto import files as files_dto
from app.application.services.files import FilesService


router = APIRouter(prefix="/files", tags=["Files"], route_class=DishkaRoute)


@router.post("/")
async def create_multiple_files(
    files_service: FromDishka[FilesService], files: list[UploadFile]
) -> dict[int | str, files_dto.FileResponse]:

    data = [
        files_dto.CreateFileRequest(name=file.filename, content=await file.read())
        for file in files
    ]

    return await files_service.create_files(data)
