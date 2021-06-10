from typing import List, Dict, Any

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

    @staticmethod
    def get_from_request(question_answer_request: AnswerVariantRequest) -> AnswerVariant:
        return AnswerVariant(name=question_answer_request.name,
                             is_right=question_answer_request.is_right)

    @classmethod
    def get_many_from_dicts(cls, answer_variants: List[Dict[str, Any]]):
        return [cls.get_from_dict(answer_variant) for answer_variant in answer_variants]

    @staticmethod
    def get_from_dict(answer_variant: Dict) -> AnswerVariant:
        return AnswerVariant(
            id=answer_variant.get('answer_variant_id'),
            name=answer_variant.get('answer_variant_text')
        )
