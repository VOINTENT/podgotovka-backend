from typing import List

from asyncpg import Record

from src.internal.biz.creators.biz.base import CreatorBiz
from src.internal.biz.creators.biz.test_question import TestQuestionCreator
from src.internal.biz.entities.biz.homework.test import HomeworkTest


class HomeworkTestCreator(CreatorBiz):
    @staticmethod
    def get_from_record(record: Record) -> HomeworkTest:
        pass

    @classmethod
    def get_from_record_many(cls, records: List[Record]) -> List[HomeworkTest]:
        return super().get_from_record_many(records)

    @staticmethod
    def get_from_questions_records(records: List[Record]) -> HomeworkTest:
        return HomeworkTest(
            test_questions=TestQuestionCreator.get_from_record_many(records)
        )
