from fastapi import FastAPI
from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from app.infrastucture import di
from app.api.v1 import all_routers
from app.config import settings
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await app.state.dishka_container.close()

app = FastAPI(title="KIUT STORAGE MICROSERVICE", lifespan=lifespan)

# app.mount("/app/media", StaticFiles(directory="./app/media"), name="media")


for router in all_routers:
    app.include_router(router, prefix=settings.api_prefix)

container = make_async_container(di.AdaptersProvider(), di.RepositoriesProvider(), di.ServicesProvider())
setup_dishka(container, app)
