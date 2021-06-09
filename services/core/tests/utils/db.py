import asyncio
import datetime
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
        TRUNCATE TABLE account_teacher, lesson_file, lesson, subject, subject_course, structure, course, lesson_view
    """)


def create_account_teacher(id: int, edited_at, email: str, name: str, hash_password: str) -> None:
    run_query("""
        INSERT INTO account_teacher(id, edited_at, email, name, hash_password) VALUES ($1, $2, $3, $4, $5)
    """, id, edited_at, email, name, hash_password)


def create_subject(id: int, name: str) -> None:
    run_query("""
        INSERT INTO subject(id, name) VALUES ($1, $2);
    """, id, name)


def create_course(id: int, name: str, structure_id: int) -> None:
    run_query("""
        INSERT INTO course(id, name, structure_id) VALUES ($1, $2, $3);
    """, id, name, structure_id)


def create_subject_course(subject_id: int, course_id: int) -> None:
    run_query("""
        INSERT INTO subject_course(subject_id, course_id) VALUES ($1, $2)
    """, subject_id, course_id)


def create_structure(id: int, name: str) -> None:
    run_query("""
        INSERT INTO structure(id, name) VALUES ($1, $2);
    """, id, name)


def create_lesson(
        id: int, name: str, description: str, youtube_link: str, time_start: datetime.datetime,
        time_finish: datetime.time, text: str, is_published: bool, subject_id, course_id: int, homework_id: int,
        account_teacher_id: int
):
    run_query(
        """
        INSERT INTO lesson(id, name, description, youtube_link, time_start, time_finish, text, is_published, subject_id,
        course_id, homework_id, account_teacher_id) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12)
        """, id, name, description, youtube_link, time_start, time_finish, text, is_published, subject_id, course_id,
        homework_id, account_teacher_id
    )
