from fastapi import APIRouter, UploadFile, File
from dishka.integrations.fastapi import FromDishka, DishkaRoute
from app.application.services.files import FilesService
from app.application.dto import files as files_dto

router = APIRouter(prefix="/files", tags=["Files"], route_class=DishkaRoute)


@router.post("/")
async def create_file(
        files_service: FromDishka[FilesService],
        upload_file: UploadFile = File(...)
) -> files_dto.FileResponse:
    data = files_dto.CreateFileRequest(
        name=upload_file.filename,
        path=f"./app/media/{upload_file.filename}"
    )
    return await files_service.create_file(data)
