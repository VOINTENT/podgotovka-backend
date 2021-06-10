from asyncpg import Record

from src.internal.biz.creators.biz.base import CreatorBiz
from src.internal.biz.creators.biz.homework.test_question import HomeworkTestQuestionCreator
from src.internal.biz.entities.biz.homework.test import HomeworkTest
from src.internal.biz.entities.request.homeworks.test.add import HomeworkTestRequest


class TestCreator(CreatorBiz):
    def get_from_record(self, record: Record):
        pass

    def get_from_request(self, homework_test_request: HomeworkTestRequest) -> HomeworkTest:
        return HomeworkTest(test_questions=[HomeworkTestQuestionCreator().get_from_request(test_question)
                                            for test_question in homework_test_request.test_questions])
