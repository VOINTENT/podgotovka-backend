from typing import Optional

from sqlalchemy import select

from src.internal.biz.dao.base import BaseDao
from src.internal.biz.dao.homework.test import HomeworkTestDao
from src.internal.biz.dao.homework.without_answer import HomeworkWithoutAnswerDao
from src.internal.biz.entities.biz.homework.homework import Homework
from src.internal.biz.entities.enum.homework_type import HomeworkTypeEnum
from src.schema.meta import homework_table, lesson_table


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
