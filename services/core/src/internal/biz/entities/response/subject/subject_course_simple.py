from pydantic import Field

from src.internal.biz.entities.response.base import BaseResponseModel


class SubjectCourseSimpleResponse(BaseResponseModel):
    name: str = Field(..., example='Русский язык (7 класс)')
    subject_id: int = Field(..., example=2)
    course_id: int = Field(..., example=5)
