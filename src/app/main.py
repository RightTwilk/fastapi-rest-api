from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.models.base import Base
from core.database import database_helper
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with database_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)
@app.get('/')
def hghgh():
    return 1


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)