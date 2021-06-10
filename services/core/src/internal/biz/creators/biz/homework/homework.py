from typing import List

from asyncpg import Record

from src.internal.biz.creators.biz.base import CreatorBiz
from src.internal.biz.creators.biz.homework.test import HomeworkTestCreator
from src.internal.biz.creators.biz.homework.without_answer import HomeworkWithoutAnswerCreator
from src.internal.biz.entities.biz.homework.homework import Homework
from src.internal.biz.entities.enum.homework_type import HomeworkTypeEnum
from src.internal.biz.entities.request.homeworks.add import HomeworkAddRequest
from src.internal.servers.http.exceptions.lesson import LessonExceptionEnum


class HomeworkCreator(CreatorBiz):
    @staticmethod
    def get_from_request(homework_request: HomeworkAddRequest) -> Homework:
        homework = Homework()

        if homework_request.homework_type == HomeworkTypeEnum.test:
            homework.homework_type = HomeworkTypeEnum.test
            homework.homework_test = HomeworkTestCreator().get_from_request(homework_request.homework_test)

        elif homework_request.homework_type == HomeworkTypeEnum.without_answer:
            homework.homework_type = HomeworkTypeEnum.without_answer
            homework.without_answer = HomeworkWithoutAnswerCreator(). \
                get_from_request(homework_request.homework_without_answer)
        else:
            raise LessonExceptionEnum.LESSON_INCORRECT_HOMEWORK_TYPE

        return homework

    @staticmethod
    def get_from_record(record: Record) -> Homework:
        return Homework(
            id=record.get('homework_id'),
            homework_type=record.get('homework_type')
        )

    @classmethod
    def get_from_record_many(cls, records: List[Record]) -> List[Homework]:
        return super().get_from_record_many(records)
