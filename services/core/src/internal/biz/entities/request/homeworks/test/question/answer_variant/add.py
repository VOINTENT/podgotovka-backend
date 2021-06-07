from pydantic import Field

from src.internal.biz.entities.request.base import BaseRequestModel


class AnswerVariantRequest(BaseRequestModel):
    name: str = Field(..., example='Текст варианта')
    is_right: bool = Field(..., example=True)
