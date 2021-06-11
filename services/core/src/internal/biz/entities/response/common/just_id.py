from pydantic import Field

from src.internal.biz.entities.response.base import BaseResponseModel


class JustIdResponse(BaseResponseModel):
    id: int = Field(..., example=1)
