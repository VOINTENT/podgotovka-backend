from pydantic import Field

from src.internal.biz.entities.response.base import BaseResponseModel


class PromptSimpleResponse(BaseResponseModel):
    id: int = Field(..., example=1)
    text: str = Field(..., example='String in JSON format')
