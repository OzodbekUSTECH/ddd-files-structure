from dishka import Provider, provide, Scope
from dishka.integrations.fastapi import FromDishka
from app.domain.protocols.uow import IUnitOfWork
from app.domain.protocols.repositories.files import IFilesRepository
from app.application.services.files import FilesService


class ServicesProvider(Provider):

    @provide(scope=Scope.REQUEST)
    def provide_files_service(
            self,
            uow: FromDishka[IUnitOfWork],
            files_repository: FromDishka[IFilesRepository]
    ) -> FilesService:
        return FilesService(
            uow=uow,
            files_repository=files_repository
        )