from typing import List

from pydantic import Field

from src.internal.biz.entities.enum.answer_type import AnswerTypeEnum
from src.internal.biz.entities.response.base import BaseResponseModel
from src.internal.biz.entities.response.answer_variant.simple import AnswerVariantSimpleResponse
from src.internal.biz.entities.response.prompt.simple import PromptSimpleResponse
from src.internal.biz.entities.response.test_question.result.previous import TestQuestionResultPreviousResponse


class TestQuestionDetailWithResultResponse(BaseResponseModel):
    question_text: str = Field(..., example='String in JSON format')
    answer_type: AnswerTypeEnum = Field(..., example='one')
    answer_variants: List[AnswerVariantSimpleResponse]
    total_count_attempts: int = Field(..., example=3)
    available_count_attempts: int = Field(..., example=2)
    used_prompts: List[PromptSimpleResponse]
    unused_prompts: List[PromptSimpleResponse]
    result: TestQuestionResultPreviousResponse
