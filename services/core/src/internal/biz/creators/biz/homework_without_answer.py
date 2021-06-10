from typing import List

from asyncpg import Record

from src.internal.biz.creators.biz.base import CreatorBiz
from src.internal.biz.entities.biz.homework.without_answer import HomeworkWithoutAnswer


class HomeworkWithoutAnswerCreator(CreatorBiz):
    @staticmethod
    def get_from_record(record: Record) -> HomeworkWithoutAnswer:
        return HomeworkWithoutAnswer(
            question=record.get('homework_without_answer_question')
        )

    @classmethod
    def get_from_record_many(cls, records: List[Record]) -> List[HomeworkWithoutAnswer]:
        return super().get_from_record_many(records)
