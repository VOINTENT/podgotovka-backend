from abc import ABC

from src.internal.biz.entities.response.base import BaseResponseModel


class TestQuestionResultAbstractResponse(BaseResponseModel, ABC):
    is_right: bool = None
    my_last_answer_variant_ids: None
    right_answer_variant_ids: None
