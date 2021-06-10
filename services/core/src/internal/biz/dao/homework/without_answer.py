from src.internal.biz.dao.base import BaseDao
from src.internal.biz.entities.biz.homework.without_answer import HomeworkWithoutAnswer
from src.schema.meta import homework_without_answer_table


class HomeworkWithoutAnswerDao(BaseDao):
    async def delete(self, without_answer_id: int) -> None:
        query = homework_without_answer_table.delete(). \
            where(homework_without_answer_table.c.id == without_answer_id)

        await self.execute(query)

    async def add(self, without_answer: HomeworkWithoutAnswer) -> int:
        query = homework_without_answer_table.insert(). \
            values(question=without_answer.question). \
            returning(homework_without_answer_table.c.id.label('without_answer_id'))

        without_answer_id = await self.fetchval(query)

        return without_answer_id
