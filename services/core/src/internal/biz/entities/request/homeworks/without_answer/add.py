from pydantic import Field

from src.internal.biz.entities.request.base import BaseRequestModel


class HomeworkWithoutAnswerRequest(BaseRequestModel):
    question: str = Field(..., example='String in JSON format')
