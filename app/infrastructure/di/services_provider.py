from dishka import Provider, Scope, provide
from dishka.integrations.fastapi import FromDishka

from app.application import services
from app.domain.protocols import repositories as interface_repos


class ServicesProvider(Provider):

    @provide(scope=Scope.REQUEST)
    def provide_files_service(
        self,
        uow: FromDishka[interface_repos.IUnitOfWork],
        files_repository: FromDishka[interface_repos.IFilesRepository],
    ) -> services.FilesService:
        return services.FilesService(uow=uow, files_repository=files_repository)
