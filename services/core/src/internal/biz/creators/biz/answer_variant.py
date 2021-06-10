from typing import Dict, Any, List

from src.internal.biz.creators.base import Creator
from src.internal.biz.entities.biz.homework.answer_variant import AnswerVariant


class AnswerVariantCreator(Creator):
    @classmethod
    def get_many_from_dicts(cls, answer_variants: List[Dict[str, Any]]):
        return [cls.get_from_dict(answer_variant) for answer_variant in answer_variants]

    @staticmethod
    def get_from_dict(answer_variant: Dict) -> AnswerVariant:
        return AnswerVariant(
            id=answer_variant.get('answer_variant_id'),
            name=answer_variant.get('answer_variant_text')
        )
