from pydantic import Field

from src.internal.biz.entities.response.base import BaseResponseModel


class AnswerVariantSimpleResponse(BaseResponseModel):
    id: int = Field(..., example=1)
    name: str = Field(..., example='Вариант ответа')
