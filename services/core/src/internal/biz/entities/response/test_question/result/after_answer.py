from typing import List, Optional

from pydantic import Field

from src.internal.biz.entities.response.test_question.result.base import TestQuestionResultAbstractResponse


class TestQuestionResultAfterAnswerResponse(TestQuestionResultAbstractResponse):
    is_right: bool = Field(..., example=True)
    my_last_answer_variant_ids: List[int] = Field(..., min_items=1)
    right_answer_variant_ids: Optional[List[int]] = Field(None, min_items=1)
