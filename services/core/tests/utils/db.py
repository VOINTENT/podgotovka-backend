import asyncio
import datetime
from typing import List, Optional

import asyncpg
from asyncpg import Record

from src.configs.db import PRIMARY_DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT


def get_dsn():
    return 'postgres://%s:%s@%s:%s/%s' % (DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, PRIMARY_DB_NAME)


def run_query(query: str, *args) -> List[Record]:
    return asyncio.get_event_loop().run_until_complete(_run(query, *args))


async def _run(query: str, *args):
    conn = await asyncpg.connect(get_dsn())
    try:
        return await conn.fetch(query, *args)
    finally:
        await conn.close()


def truncate_tables():
    run_query("""
        TRUNCATE TABLE 
            account_teacher, 
            account_student, 
            course, 
            subject, 
            subject_course, 
            lesson, 
            lesson_file, 
            homework, 
            homework_without_answer, 
            homework_test, 
            test_question, 
            prompt, 
            answer_variant, 
            lesson_view, 
            subject_course_subscription,
            subject_course_lead
    """)


def create_account_teacher(id: int, edited_at, email: str, name: str, hash_password: str) -> None:
    run_query("""
        INSERT INTO account_teacher(id, edited_at, email, name, hash_password) VALUES ($1, $2, $3, $4, $5)
    """, id, edited_at, email, name, hash_password)


def create_account_student(id: int, edited_at, email: str, name: str, hash_password: str) -> None:
    run_query("""
        INSERT INTO account_student(id, edited_at, email, name, hash_password) VALUES ($1, $2, $3, $4, $5)
    """, id, edited_at, email, name, hash_password)


def create_account_student_vk(id: int, edited_at, email: str, name: str, last_name: str, vk_id: int) -> None:
    run_query("""
        INSERT INTO account_student(id, edited_at, email, name, last_name, vk_id) VALUES ($1, $2, $3, $4, $5, $6)
    """, id, edited_at, email, name, last_name, vk_id)


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


def create_subject_course_with_id(id: int, subject_id: int, course_id: int) -> None:
    run_query("""
        INSERT INTO subject_course(id, subject_id, course_id) VALUES ($1, $2, $3)
    """, id, subject_id, course_id)


def create_subject_course_lead(account_teacher_id: int, subject_course_id: int) -> None:
    run_query("""
            INSERT INTO subject_course_lead(account_teacher_id, subject_course_id) VALUES ($1, $2)
        """, account_teacher_id, subject_course_id)


def create_subject_course_subscribed(account_student_id: int, subject_course_id: int) -> None:
    run_query("""
            INSERT INTO subject_course_subscription(account_student_id, subject_course_id) VALUES ($1, $2)
        """, account_student_id, subject_course_id)


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


def create_homework(id: int, homework_type: str, homework_without_answer_id: Optional[int],
                    homework_test_id: Optional[int]):
    run_query("""
        INSERT INTO homework(id, homework_type, homework_without_answer_id, homework_test_id) VALUES ($1, $2, $3, $4)
    """, id, homework_type, homework_without_answer_id, homework_test_id)


def create_homework_test(id: int):
    run_query("""INSERT INTO homework_test(id) VALUES ($1)""", id)


def create_test_question(id: int, homework_test_id: int, name: str, description: str, answer_type: str,
                         count_attempts: int):
    run_query("""
        INSERT INTO test_question(id, homework_test_id, name, description, answer_type, count_attempts)
        VALUES ($1, $2, $3, $4, $5, $6)
    """, id, homework_test_id, name, description, answer_type, count_attempts)


def create_lesson_file(id: int, name: str, file_link: str, lesson_id: int):
    run_query("""
        INSERT INTO lesson_file(id, name, file_link, lesson_id) VALUES ($1, $2, $3, $4)
    """, id, name, file_link, lesson_id)


def create_answer_variant(id: int, name: str, is_right: bool, test_question_id: int):
    run_query("""
        INSERT INTO answer_variant(id, text, is_right, test_question_id) VALUES ($1, $2, $3, $4)
    """, id, name, is_right, test_question_id)
