from typing import Optional, List

from pydantic.fields import Field

from src.internal.biz.entities.enum.answer_type import AnswerTypeEnum
from src.internal.biz.entities.response.answer_variant.simple import AnswerVariantSimpleResponse
from src.internal.biz.entities.response.base import BaseResponseModel
from src.internal.biz.entities.response.prompt.simple import PromptSimpleResponse


class TestQuestionDetailResponse(BaseResponseModel):
    question_text: str = Field(..., example='String in JSON format')
    answer_type: AnswerTypeEnum = Field(..., example='one')
    answer_variants: Optional[List[AnswerVariantSimpleResponse]] = Field(None, min_items=1)
    total_count_attempts: int = Field(..., example=3)
    prompts: List[PromptSimpleResponse]
