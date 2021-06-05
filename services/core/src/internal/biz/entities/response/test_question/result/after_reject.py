from typing import List

from pydantic import Field

from src.internal.biz.entities.response.test_question.result.base import TestQuestionResultAbstractResponse


class TestQuestionResultAfterRejectResponse(TestQuestionResultAbstractResponse):
    is_right: bool = False
    my_last_answer_variant_ids: None
    right_answer_variant_ids: List[int] = Field(..., min_items=1)
