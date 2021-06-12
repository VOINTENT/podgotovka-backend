from pydantic import Field

from src.internal.biz.entities.response.base import BaseResponseModel


class SubjectSimpleResponse(BaseResponseModel):
    id: int = Field(..., example=1)
    name: str = Field(..., example='Название')
