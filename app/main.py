from contextlib import asynccontextmanager

from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.v1 import all_routers
from app.infrastructure import di
from app.infrastructure.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await app.state.dishka_container.close()


app = FastAPI(title="KIUT ACCOUNTING MICROSERVICE", lifespan=lifespan)

app.mount("/app/media", StaticFiles(directory="./app/media"), name="media")


for router in all_routers:
    app.include_router(router, prefix=settings.api_prefix)

container = make_async_container(
    di.AdaptersProvider(), di.RepositoriesProvider(), di.InteractorsProvider()
)
setup_dishka(container, app)
