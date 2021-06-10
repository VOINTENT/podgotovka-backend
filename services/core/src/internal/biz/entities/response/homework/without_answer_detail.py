from typing import Optional

from pydantic import Field

from src.internal.biz.entities.response.base import BaseResponseModel


class HomeworkWithoutAnswerDetailResponse(BaseResponseModel):
    question: Optional[str] = Field(None, example='String in JSON format')
