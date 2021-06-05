from pydantic import Field

from src.internal.biz.entities.request.base import BaseRequestModel


class TestQuestionAnswerRequest(BaseRequestModel):
    question_id: int = Field(..., example=1)
    variant_id: int = Field(..., example=2)
