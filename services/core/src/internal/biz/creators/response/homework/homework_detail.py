from typing import List

from src.internal.biz.creators.base import Creator
from src.internal.biz.creators.response.homework.homework_test_detail import HomeworkTestDetailResponseCreator
from src.internal.biz.creators.response.homework.homework_without_answer_detail import \
    HomeworkWithoutAnswerDetailResponseCreator
from src.internal.biz.entities.biz.homework.homework import Homework
from src.internal.biz.entities.response.homework.detail import HomeworkDetailResponse


class HomeworkDetailResponseCreator(Creator):
    @classmethod
    def get_from_one(cls, homework: Homework) -> HomeworkDetailResponse:
        if homework.without_answer:
            homework.without_answer = HomeworkWithoutAnswerDetailResponseCreator().get_from_one(homework.without_answer)
        if homework.homework_test:
            homework.homework_test = HomeworkTestDetailResponseCreator().get_from_one(homework.homework_test)
        return HomeworkDetailResponse(
            id=homework.id,
            type=homework.homework_type,
            homework_without_answer=homework.without_answer,
            homework_test=homework.homework_test
        )

    @classmethod
    def get_from_many(cls, homeworks: List[Homework]) -> List[HomeworkDetailResponse]:
        return [cls.get_from_one(homework) for homework in homeworks]
