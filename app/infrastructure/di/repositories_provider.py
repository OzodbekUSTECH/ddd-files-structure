from dishka import Provider, Scope, provide
from dishka.integrations.fastapi import FromDishka
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.protocols import repositories as interface_repos
from app.infrastructure.repositories import sqlalchemy as sa_repos


class RepositoriesProvider(Provider):

    @provide(scope=Scope.REQUEST)
    def provide_uow(
        self, session: FromDishka[AsyncSession]
    ) -> interface_repos.IUnitOfWork:
        return sa_repos.SqlalchemyUnitOfWork(session=session)
