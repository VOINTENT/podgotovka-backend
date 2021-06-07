from typing import List, Optional

from pydantic import Field

from src.internal.biz.entities.response.test_question.result.base import TestQuestionResultAbstractResponse


class TestQuestionResultPreviousResponse(TestQuestionResultAbstractResponse):
    is_right: Optional[bool] = Field(None, example=True)
    my_last_answer_variant_ids: Optional[List[int]] = Field(None, min_items=1)
    right_answer_variant_ids: Optional[List[int]] = Field(None, min_items=1)
