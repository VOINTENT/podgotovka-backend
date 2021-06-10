from typing import List

from src.internal.biz.creators.base import Creator
from src.internal.biz.entities.biz.homework.answer_variant import AnswerVariant
from src.internal.biz.entities.response.answer_variant.simple import AnswerVariantSimpleResponse


class AnswerVariantSimpleResponseCreator(Creator):
    @classmethod
    def get_many_from_answer_variants(cls, answer_variants: List[AnswerVariant]) -> List[AnswerVariantSimpleResponse]:
        return [cls.get_from_answer_variant(answer_variant) for answer_variant in answer_variants]

    @staticmethod
    def get_from_answer_variant(answer_variant: AnswerVariant) -> AnswerVariantSimpleResponse:
        return AnswerVariantSimpleResponse(
            id=answer_variant.id,
            name=answer_variant.name
        )
