from dishka import Provider, Scope, provide
from dishka.integrations.fastapi import FromDishka

from app.application import interactors
from app.domain.protocols import repositories as interface_repos


class InteractorsProvider(Provider):
    pass
