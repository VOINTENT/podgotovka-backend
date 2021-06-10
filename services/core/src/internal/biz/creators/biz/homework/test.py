from typing import List

from asyncpg import Record

from src.internal.biz.creators.biz.base import CreatorBiz
from src.internal.biz.creators.biz.homework.test_question import TestQuestionCreator
from src.internal.biz.entities.biz.homework.test import HomeworkTest
from src.internal.biz.entities.request.homeworks.test.add import HomeworkTestRequest


class HomeworkTestCreator(CreatorBiz):
    @staticmethod
    def get_from_record(record: Record):
        pass

    @staticmethod
    def get_from_request(homework_test_request: HomeworkTestRequest) -> HomeworkTest:
        return HomeworkTest(test_questions=[TestQuestionCreator().get_from_request(test_question)
                                            for test_question in homework_test_request.test_questions])

    @staticmethod
    def get_from_questions_records(records: List[Record]) -> HomeworkTest:
        return HomeworkTest(
            test_questions=TestQuestionCreator.get_from_record_many(records)
        )
