from pydantic import Field

from src.internal.biz.entities.request.base import BaseRequestModel


class PromptRequest(BaseRequestModel):
    name: str = Field(..., example='String in JSON format')
