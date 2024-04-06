from dishka import Provider, provide, Scope
from dishka.integrations.fastapi import FromDishka
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.protocols.uow import IUnitOfWork
from app.domain.protocols.repositories.files import IFilesRepository
from app.infrastucture.repositories.sqlalchemy.uow import SqlalchemyUnitOfWork
from app.infrastucture.repositories.sqlalchemy.files import SqlalchemyFilesRepository


class RepositoriesProvider(Provider):

    @provide(scope=Scope.REQUEST)
    def provide_uow(
            self,
            session: FromDishka[AsyncSession]
    ) -> IUnitOfWork:
        return SqlalchemyUnitOfWork(session=session)

    @provide(scope=Scope.REQUEST)
    def provide_files_repository(
            self,
            session: FromDishka[AsyncSession]
    ) -> IFilesRepository:
        return SqlalchemyFilesRepository(session=session)