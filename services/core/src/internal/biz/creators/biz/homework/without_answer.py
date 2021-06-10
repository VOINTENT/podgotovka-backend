from asyncpg import Record

from src.internal.biz.creators.biz.base import CreatorBiz
from src.internal.biz.entities.biz.homework.without_answer import HomeworkWithoutAnswer
from src.internal.biz.entities.request.homeworks.without_answer.add import HomeworkWithoutAnswerRequest


class HomeworkWithoutAnswerCreator(CreatorBiz):
    @staticmethod
    def get_from_record(record: Record):
        pass

    def get_from_request(self, homework_without_answer: HomeworkWithoutAnswerRequest) -> HomeworkWithoutAnswer:
        return HomeworkWithoutAnswer(question=homework_without_answer.question)
