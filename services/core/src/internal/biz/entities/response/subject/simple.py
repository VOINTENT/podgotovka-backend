from pydantic import Field

from src.internal.biz.entities.response.base import BaseResponseModel


class SubjectSimpleResponse(BaseResponseModel):
    name: str = Field(None, example='Название')
    course_id: int = Field(..., example=1)
    subject_id: int = Field(..., example=2)
