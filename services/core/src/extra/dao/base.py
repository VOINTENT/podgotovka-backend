from abc import ABC, abstractmethod
from contextlib import asynccontextmanager

from asyncpg import Connection
from asyncpg.pool import Pool

from src.internal.drivers.async_pg import AsyncPg


class BaseLogsDao(ABC):

    def __init__(self, conn: Connection = None) -> None:
        self.__pool: Pool = AsyncPg.get_pool_log_db()
        self.__conn: Connection = conn

    async def _get_connection_from_pool(self) -> Connection:
        return await self.__pool.acquire()

    async def _set_back_connection_to_pool(self, conn: Connection) -> None:
        await self.__pool.release(conn)

    @property
    @asynccontextmanager
    async def _connection(self):
        conn = await self._get_connection_from_pool()
        try:
            yield conn
        except Exception:
            raise
        finally:
            await self._set_back_connection_to_pool(conn)

    async def execute(self, query, *args) -> None:
        async with self._connection as conn:
            await conn.execute(query, *args)

    @abstractmethod
    async def add(self, obj):
        pass
