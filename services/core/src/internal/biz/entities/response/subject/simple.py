from pydantic import Field

from src.internal.biz.entities.response.base import BaseResponseModel


class SubjectSimpleResponse(BaseResponseModel):
    id: int = Field(None, example=1)
    name: str = Field(None, example='Название')
