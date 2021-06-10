from src.internal.biz.creators.base import Creator
from src.internal.biz.entities.biz.homework.without_answer import HomeworkWithoutAnswer
from src.internal.biz.entities.response.homework.without_answer_detail import HomeworkWithoutAnswerDetailResponse


class HomeworkWithoutAnswerDetailResponseCreator(Creator):
    @staticmethod
    def get_from_homework_without_answer(
            homework_without_answer: HomeworkWithoutAnswer) -> HomeworkWithoutAnswerDetailResponse:
        return HomeworkWithoutAnswerDetailResponse(
            question=homework_without_answer.question
        )
