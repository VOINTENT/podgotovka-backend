from pydantic import Field

from src.internal.biz.entities.response.base import BaseResponseModel


class HomeworkWithoutAnswerDetailResponse(BaseResponseModel):
    question: str = Field(..., example='String in JSON format')
