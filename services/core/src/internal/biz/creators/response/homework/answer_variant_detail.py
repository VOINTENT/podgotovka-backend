from typing import List

from src.internal.biz.creators.base import Creator
from src.internal.biz.entities.biz.homework.answer_variant import AnswerVariant
from src.internal.biz.entities.response.answer_variant.simple import AnswerVariantSimpleResponse


class QuestionAnswerVariantResponseCreator(Creator):
    @classmethod
    def get_from_one(cls, answer_variant: AnswerVariant) -> AnswerVariantSimpleResponse:
        return AnswerVariantSimpleResponse(
            id=answer_variant.id,
            name=answer_variant.name
        )

    @classmethod
    def get_from_many(cls, answer_variants: List[AnswerVariant]) -> List[AnswerVariantSimpleResponse]:
        return [cls.get_from_one(answer_variant) for answer_variant in answer_variants]
