from src.internal.biz.creators.base import Creator
from src.internal.biz.creators.response.test_question_detail_response import TestQuestionDetailWithResultResponseCreator
from src.internal.biz.entities.biz.homework.test import HomeworkTest
from src.internal.biz.entities.response.homework.test_detail_with_results import HomeworkTestDetailWithResultsResponse


class HomeworkTestDetailWithResultsResponseCreator(Creator):
    @staticmethod
    def get_from_homework_test(homework_test: HomeworkTest) -> HomeworkTestDetailWithResultsResponse:
        return HomeworkTestDetailWithResultsResponse(
            test_questions=TestQuestionDetailWithResultResponseCreator.get_many_from_test_questions(
                homework_test.test_questions)
        )
