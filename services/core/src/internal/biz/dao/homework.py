from typing import Optional, cast

from sqlalchemy import select, Column, func, String, text, JSON
from sqlalchemy.sql import Select
from sqlalchemy.sql.functions import coalesce

from src.internal.biz.creators.biz.homework import HomeworkCreator
from src.internal.biz.creators.biz.homework_test import HomeworkTestCreator
from src.internal.biz.creators.biz.homework_without_answer import HomeworkWithoutAnswerCreator
from src.internal.biz.dao.base import BaseDao
from src.internal.biz.entities.biz.homework.homework import Homework
from src.internal.biz.entities.biz.homework.test import HomeworkTest
from src.internal.biz.entities.biz.homework.without_answer import HomeworkWithoutAnswer
from src.internal.biz.entities.enum.homework_type import HomeworkTypeEnum
from src.schema.meta import homework_table, homework_without_answer_table, homework_test_table, test_question_table, \
    prompt_table, answer_variant_table


class HomeworkDao(BaseDao):
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
