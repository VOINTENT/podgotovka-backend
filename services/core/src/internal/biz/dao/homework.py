from typing import Optional

from sqlalchemy import select

from src.internal.biz.creators.biz.homework import HomeworkCreator
from src.internal.biz.creators.biz.homework_without_answer import HomeworkWithoutAnswerCreator
from src.internal.biz.dao.base import BaseDao
from src.internal.biz.entities.biz.homework.homework import Homework
from src.internal.biz.entities.biz.homework.test import HomeworkTest
from src.internal.biz.entities.biz.homework.without_answer import HomeworkWithoutAnswer
from src.internal.biz.entities.enum.homework_type import HomeworkTypeEnum
from src.schema.meta import homework_table, homework_without_answer_table


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

    async def get_homework_test(self, homework_id: int, account_student_id: int) -> HomeworkTest:
        pass
