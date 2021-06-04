from abc import ABC, abstractmethod
from contextlib import asynccontextmanager
from typing import Optional, List, Any

from asyncpg import Connection, Pool, Record

from src.internal.drivers.async_pg import AsyncPg


class BaseDao(ABC):
    def __init__(self, conn: Optional[Connection] = None) -> None:
        self.__pool: Pool = AsyncPg.get_pool_primary_db()
        self.__conn = conn

    async def _get_connection_from_pool(self) -> Connection:
        return await self.__pool.acquire()

    async def _set_back_connection_to_pool(self, conn: Connection) -> None:
        await self.__pool.release(conn)

    @property
    @asynccontextmanager
    async def _connection(self):
        if self.__conn:
            yield self.__conn
        else:
            conn = await self._get_connection_from_pool()
            try:
                yield conn
            except Exception:
                raise
            finally:
                await self._set_back_connection_to_pool(conn)

    @asynccontextmanager
    async def connection_transaction(self):
        connection = await self._get_connection_from_pool()
        transaction = connection.transaction()
        await transaction.start()
        try:
            yield connection
        except Exception:
            await transaction.rollback()
            raise
        else:
            await transaction.commit()
        finally:
            await self._set_back_connection_to_pool(connection)

    async def execute(self, query) -> None:
        async with self._connection as conn:
            await conn.execute(query)

    async def fetchall(self, query) -> List[Record]:
        async with self._connection as conn:
            return await conn.fetch(query)

    async def fetchone(self, query) -> Record:
        async with self._connection as conn:
            return await conn.fetchrow(query)

    async def fetchval(self, query) -> Any:
        async with self._connection as conn:
            return await conn.fetchval(query)

    @abstractmethod
    async def add(self, obj):
        pass

    @abstractmethod
    async def add_many(self, obj):
        pass

    @abstractmethod
    async def get_by_id(self, id):
        pass

    @abstractmethod
    async def get_all(self, limit: Optional[int] = 1_000_000, offset: Optional[int] = 0):
        pass

    @abstractmethod
    async def update(self, id, obj):
        pass

    @abstractmethod
    async def remove_by_id(self, id):
        pass
