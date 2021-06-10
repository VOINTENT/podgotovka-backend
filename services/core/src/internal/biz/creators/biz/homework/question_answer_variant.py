from asyncpg import Record

from src.internal.biz.creators.biz.base import CreatorBiz
from src.internal.biz.entities.biz.homework.answer_variant import AnswerVariant
from src.internal.biz.entities.request.homeworks.test.question.answer_variant.add import AnswerVariantRequest


class AnswerVariantCreator(CreatorBiz):
    @staticmethod
    def get_from_record(record: Record):
        return AnswerVariant(id=record.get('answer_variant_id'),
                             name=record.get('answer_variant_text'),
                             is_right=record.get('answer_variant_is_right'))

    def get_from_request(self, question_answer_request: AnswerVariantRequest) -> AnswerVariant:
        return AnswerVariant(name=question_answer_request.name,
                             is_right=question_answer_request.is_right)
