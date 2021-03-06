from abc import ABC
from contextlib import asynccontextmanager
from typing import Optional, List, Any

from asyncpg import Connection, Pool, Record
from sqlalchemy.sql import Select

from src.internal.drivers.async_pg import AsyncPg


class BaseDao(ABC):
    def __init__(self, conn: Optional[Connection] = None) -> None:
        self.__pool: Pool = AsyncPg.get_pool_primary_db()
        self.__conn = conn

    @property
    def conn(self) -> Connection:
        return self.__conn

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

    @staticmethod
    def _add_pagination(query: Select, limit: int = 1_000_000, offset: int = 0) -> Select:
        return query.limit(limit).offset(offset)
