from fastapi import FastAPI
from contextlib import asynccontextmanager
from models.base import Base
from core.database import database_helper

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with database_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)
