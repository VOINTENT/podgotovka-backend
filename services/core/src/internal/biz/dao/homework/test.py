from typing import Optional, List

from src.internal.biz.creators.biz.homework.question_answer_variant import AnswerVariantCreator
from src.internal.biz.creators.biz.homework.question_prompt import PromptCreator
from src.internal.biz.dao.base import BaseDao
from src.internal.biz.entities.biz.homework.answer_variant import AnswerVariant
from src.internal.biz.entities.biz.homework.prompt import Prompt
from src.internal.biz.entities.biz.homework.test import HomeworkTest
from src.internal.biz.entities.biz.homework.test_question import TestQuestion
from src.schema.meta import prompt_table, answer_variant_table, test_question_table, homework_test_table


class HomeworkTestDao(BaseDao):
    async def delete(self, test_id: int) -> None:
        query = homework_test_table.delete(). \
            where(homework_test_table.c.id == test_id)

        await self.execute(query)

    async def add(self, homework_test: HomeworkTest) -> Optional[HomeworkTest]:
        query = homework_test_table.insert(). \
            returning(homework_test_table.c.id.label('homework_test_id'))

        row = await self.fetchone(query)

        homework_test_id = row['homework_test_id']
        homework_test.id = homework_test_id

        homework_test.test_questions = [await self.add_question(question, homework_test_id)
                                        for question in homework_test.test_questions]

        return homework_test

    async def add_question(self, question: TestQuestion, homework_test_id: int) -> Optional[TestQuestion]:
        query = test_question_table.insert(). \
            values(homework_test_id=homework_test_id,
                   description=question.text,
                   answer_type=question.answer_type,
                   count_attempts=question.count_attempts). \
            returning(test_question_table.c.id.label('test_question_id'))

        row = await self.fetchone(query)

        question_id = row['test_question_id']

        question.prompts = await self.add_prompts(question.prompts, question_id)
        question.answer_variants = await self.add_answer_variants(question.answer_variants, question_id)

        return question

    async def add_prompts(self, prompts: List[Prompt], test_question_id: int) -> List[Prompt]:
        query = prompt_table.insert(). \
            values([{"test_question_id": test_question_id,
                     "text": prompt.text}
                    for prompt in prompts]). \
            returning(prompt_table.c.id.label('prompt_id'),
                      prompt_table.c.text.label('prompt_text'),
                      prompt_table.c.test_question_id.label('test_question_id'))

        rows = await self.fetchall(query)
        return PromptCreator.get_from_record_many(rows)

    async def add_answer_variants(self, answers: List[AnswerVariant], test_question_id: int) -> List[AnswerVariant]:
        query = answer_variant_table.insert(). \
            values([{"test_question_id": test_question_id,
                     "text": answer.name,
                     "is_right": answer.is_right}
                    for answer in answers]). \
            returning(answer_variant_table.c.id.label('answer_variant_id'),
                      answer_variant_table.c.text.label('answer_variant_text'),
                      answer_variant_table.c.is_right.label('answer_variant_is_right'))

        rows = await self.fetchall(query)
        return AnswerVariantCreator.get_from_record_many(rows)
