from src.internal.biz.creators.base import Creator
from src.internal.biz.creators.response.homework_test_detail_with_results_response import \
    HomeworkTestDetailWithResultsResponseCreator
from src.internal.biz.creators.response.homework_without_answer_detail_response import \
    HomeworkWithoutAnswerDetailResponseCreator
from src.internal.biz.entities.biz.homework.homework import Homework
from src.internal.biz.entities.response.homework.detail_with_results import HomeworkDetailWithResultsResponse


class HomeworkDetailWithResultsResponseCreator(Creator):
    @staticmethod
    def get_from_homework(homework: Homework) -> HomeworkDetailWithResultsResponse:
        return HomeworkDetailWithResultsResponse(
            id=homework.id,
            type=homework.homework_type,
            homework_without_answer=HomeworkWithoutAnswerDetailResponseCreator.get_from_homework_without_answer(
                homework.without_answer) if homework.without_answer else None,
            homework_test=HomeworkTestDetailWithResultsResponseCreator.get_from_homework_test(
                homework.homework_test) if homework.homework_test else None
        )
