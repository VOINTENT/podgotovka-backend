from typing import List, Optional

from pydantic import Field

from src.internal.biz.entities.enum.answer_type import AnswerTypeEnum
from src.internal.biz.entities.request.base import BaseRequestModel
from src.internal.biz.entities.request.homeworks.test.question.answer_variant.add import AnswerVariantRequest
from src.internal.biz.entities.request.homeworks.test.question.prompt.add import PromptRequest


class TestQuestionRequest(BaseRequestModel):
    question_text: str = Field(..., example='String in JSON format')
    answer_type: AnswerTypeEnum = Field(..., example='one')
    answer_variants: Optional[List[AnswerVariantRequest]] = Field(None, min_items=1)
    total_count_attempts: int = Field(..., example=3)
    prompts: List[PromptRequest]
