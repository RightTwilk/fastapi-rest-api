from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.models.base import Base
from core.database import database_helper
from app.items.router import item_router
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with database_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(item_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
