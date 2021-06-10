from typing import List

from src.internal.biz.creators.base import Creator
from src.internal.biz.creators.response.homework.question_detail import TestQuestionResponseCreator
from src.internal.biz.entities.biz.homework.test import HomeworkTest
from src.internal.biz.entities.response.homework.test_detail import HomeworkTestDetailResponse


class HomeworkTestDetailResponseCreator(Creator):
    @classmethod
    def get_from_one(cls, home_test: HomeworkTest) -> HomeworkTestDetailResponse:
        test_questions = TestQuestionResponseCreator().get_from_many(home_test.test_questions)
        return HomeworkTestDetailResponse(
            test_questions=test_questions
        )

    @classmethod
    def get_from_many(cls, home_tests: List[HomeworkTest]) -> List[HomeworkTestDetailResponse]:
        return [cls.get_from_one(home_test) for home_test in home_tests]
