import asyncio
from typing import List

import asyncpg
from asyncpg import Record

from src.configs.db import PRIMARY_DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT


def get_dsn():
    return 'postgres://%s:%s@%s:%s/%s' % (DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, PRIMARY_DB_NAME)


def run_query(query: str, *args) -> List[Record]:
    return asyncio.get_event_loop().run_until_complete(_run(query, *args))


async def _run(query: str, *args):
    conn = await asyncpg.connect(get_dsn())
    return await conn.fetch(query, *args)


def truncate_tables():
    run_query("""
        TRUNCATE TABLE test
    """)
