import json
from typing import List

from asyncpg import Record

from src.internal.biz.creators.biz.answer_variant import AnswerVariantCreator
from src.internal.biz.creators.biz.base import CreatorBiz
from src.internal.biz.creators.biz.prompt import PromptCreator
from src.internal.biz.entities.biz.homework.test_question import TestQuestion


class TestQuestionCreator(CreatorBiz):
    @staticmethod
    def get_from_record(record: Record) -> TestQuestion:
        return TestQuestion(
            id=record.get('test_question_id'),
            name=record.get('test_question_name'),
            text=record.get('test_question_text'),
            answer_type=record.get('test_question_answer_type'),
            count_attempts=record.get('test_question_count_attempts'),
            prompts=PromptCreator.get_many_from_dicts(
                json.loads(record['test_question_prompts'])) if 'test_question_prompts' in record else [],
            answer_variants=AnswerVariantCreator.get_many_from_dicts(
                json.loads(
                    record['test_question_answer_variants'])) if 'test_question_answer_variants' in record else []
        )

    @classmethod
    def get_from_record_many(cls, records: List[Record]) -> List[TestQuestion]:
        return super().get_from_record_many(records)
