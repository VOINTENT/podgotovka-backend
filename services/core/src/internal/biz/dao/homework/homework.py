from typing import Optional

from sqlalchemy import select, Column, text, func
from sqlalchemy.sql import Select
from sqlalchemy.sql.functions import coalesce

from src.internal.biz.creators.biz.homework.homework import HomeworkCreator
from src.internal.biz.creators.biz.homework.test import HomeworkTestCreator
from src.internal.biz.creators.biz.homework.without_answer import HomeworkWithoutAnswerCreator
from src.internal.biz.dao.base import BaseDao
from src.internal.biz.dao.homework.test import HomeworkTestDao
from src.internal.biz.dao.homework.without_answer import HomeworkWithoutAnswerDao
from src.internal.biz.entities.biz.homework.homework import Homework
from src.internal.biz.entities.biz.homework.test import HomeworkTest
from src.internal.biz.entities.biz.homework.without_answer import HomeworkWithoutAnswer
from src.internal.biz.entities.enum.homework_type import HomeworkTypeEnum
from src.schema.meta import homework_table, lesson_table, homework_without_answer_table, test_question_table, \
    homework_test_table, prompt_table, answer_variant_table


class HomeworkDao(BaseDao):
    async def delete(self, homework_id: int) -> None:
        query = homework_table.delete(). \
            where(homework_table.c.id == homework_id)
        await self.execute(query)

    async def delete_deep(self, homework_id: int) -> None:

        query_without_and_test_id = select([homework_table.c.homework_without_answer_id,
                                            homework_table.c.homework_test_id]). \
            where(homework_table.c.id == homework_id)

        ids = await self.fetchone(query_without_and_test_id)

        if not ids:
            return

        without_answer_id, test_id = ids['homework_without_answer_id'], ids['homework_test_id']

        async with self._connection as conn:
            if test_id:
                await HomeworkTestDao(conn).delete(test_id)
            if without_answer_id:
                await HomeworkWithoutAnswerDao(conn).delete(without_answer_id)

    async def exist(self, lesson_id: int) -> Optional[int]:
        query = select([lesson_table.c.homework_id.label('lesson_homework_id')]). \
            where(lesson_table.c.id == lesson_id)

        row = await self.fetchone(query)

        if not row:
            return None

        return row['lesson_homework_id']

    async def add(self, homework: Homework) -> Optional[Homework]:
        async with self._connection as conn:
            query = homework_table.insert()
            if homework.homework_type == HomeworkTypeEnum.test:
                homework.homework_test = await HomeworkTestDao(conn).add(homework.homework_test)
                query = query. \
                    values(homework_type=homework.homework_type,
                           homework_test_id=homework.homework_test.id)

            elif homework.homework_type == HomeworkTypeEnum.without_answer:
                without_answer_id = await HomeworkWithoutAnswerDao(conn).add(homework.without_answer)
                query = query. \
                    values(homework_type=homework.homework_type,
                           homework_without_answer_id=without_answer_id)
            else:
                raise

        query = query.returning(homework_table.c.id.label('homework_id'))
        row = await self.fetchone(query)
        homework.id = row['homework_id']

        return homework

    async def get_detail_for_student(self, homework_id: int, account_student_id: Optional[int]) -> Optional[Homework]:
        homework = await self.get_homework_simple(homework_id)
        if not homework:
            return None

        if homework.homework_type == HomeworkTypeEnum.without_answer:
            homework.without_answer = await self.get_homework_without_answer(homework_id)
        elif homework.homework_type == HomeworkTypeEnum.test:
            homework.homework_test = await self.get_homework_test(homework_id, account_student_id)
        return homework

    async def get_homework_simple(self, homework_id: int) -> Optional[Homework]:
        query = select([
            homework_table.c.id.label('homework_id'),
            homework_table.c.homework_type.label('homework_type'),
        ]).select_from(
            homework_table
        ).where(
            homework_table.c.id == homework_id
        )

        row = await self.fetchone(query)
        if not row:
            return None
        return HomeworkCreator.get_from_record(row)

    async def get_homework_without_answer(self, homework_id) -> HomeworkWithoutAnswer:
        query = select([
            homework_without_answer_table.question.lable('homework_without_answer_question')
        ]).select_from(
            homework_table.join(homework_without_answer_table)
        ).where(
            homework_table.c.id == homework_id
        )

        row = await self.fetchone(query)
        return HomeworkWithoutAnswerCreator.get_from_record(row)

    async def get_homework_test(self, homework_id: int, account_student_id: int) -> Optional[HomeworkTest]:
        query = select([
            test_question_table.c.id.label('test_question_id'),
            test_question_table.c.name.label('test_question_name'),
            test_question_table.c.description.label('test_question_text'),
            test_question_table.c.answer_type.label('test_question_answer_type'),
            test_question_table.c.count_attempts.label('test_question_count_attempts'),
            self.__class__._get_select_prompts(test_question_table.c.id).as_scalar().label('test_question_prompts'),
            self.__class__._get_select_answer_variants(test_question_table.c.id).as_scalar().label(
                'test_question_answer_variants')
        ]).select_from(
            homework_table.join(
                homework_test_table
            ).join(
                test_question_table
            )
        ).where(
            homework_table.c.id == homework_id
        )

        rows = await self.fetchall(query)
        if not rows:
            return None
        return HomeworkTestCreator.get_from_questions_records(rows)

    @staticmethod
    def _get_select_prompts(test_question_id: Column) -> Select:
        return select([coalesce(func.json_agg(func.json_build_object(
            text("'prompt_text'"), prompt_table.c.text
        )), text("'[]'::json"))]).select_from(
            prompt_table
        ).where(
            prompt_table.c.test_question_id == test_question_id
        )

    @staticmethod
    def _get_select_answer_variants(test_question_id: Column) -> Select:
        return select([func.coalesce(func.json_agg(func.json_build_object(
            text("'answer_variant_id'"), answer_variant_table.c.id,
            text("'answer_variant_text'"), answer_variant_table.c.text
        )), text("'[]'::json"))]).select_from(
            answer_variant_table
        ).where(
            answer_variant_table.c.test_question_id == test_question_id
        )
