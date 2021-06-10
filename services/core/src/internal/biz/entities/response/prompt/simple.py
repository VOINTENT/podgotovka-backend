from pydantic import Field

from src.internal.biz.entities.response.base import BaseResponseModel


class PromptSimpleResponse(BaseResponseModel):
    text: str = Field(..., example='String in JSON format')
