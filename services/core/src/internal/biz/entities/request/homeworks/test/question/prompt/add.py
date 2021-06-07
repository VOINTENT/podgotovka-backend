from pydantic import Field

from src.internal.biz.entities.request.base import BaseRequestModel


class PromptRequest(BaseRequestModel):
    text: str = Field(..., example='String in JSON format')
