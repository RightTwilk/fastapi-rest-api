from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from core.config import settings



class DatabaseHelper():
    def __init__(self):
        self.engine = create_async_engine(
            url=settings.DATABASE_URL,
            echo = settings.ECHO
            )
        self.session_creator = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            expire_on_commit=False,
        )