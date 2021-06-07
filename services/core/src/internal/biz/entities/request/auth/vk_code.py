from pydantic import Field

from src.internal.biz.entities.request.base import BaseRequestModel


class VkCodeRequest(BaseRequestModel):
    code: str = Field(..., example='qwerty123', min_length=10, max_length=1000)
