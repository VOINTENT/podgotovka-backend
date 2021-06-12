from pydantic import Field

from src.internal.biz.entities.response.base import BaseResponseModel


class SubjectCustomResponse(BaseResponseModel):
    name: str = Field(..., example='Физика (11 класс)')
    course_id: int = Field(..., example=1)
    subject_id: int = Field(..., example=1)
