from typing import List, Optional

from src.internal.biz.creators.base import Creator
from src.internal.biz.entities.biz.homework.without_answer import HomeworkWithoutAnswer
from src.internal.biz.entities.response.homework.without_answer_detail import HomeworkWithoutAnswerDetailResponse


class HomeworkWithoutAnswerDetailResponseCreator(Creator):
    @classmethod
    def get_from_one(cls, without_answer: HomeworkWithoutAnswer) -> Optional[HomeworkWithoutAnswerDetailResponse]:
        if not without_answer:
            return None
        return HomeworkWithoutAnswerDetailResponse(
            question=without_answer.question
        )

    @classmethod
    def get_from_many(cls, without_answers: List[HomeworkWithoutAnswer]) -> List[HomeworkWithoutAnswerDetailResponse]:
        return [cls.get_from_one(without_answer) for without_answer in without_answers]
