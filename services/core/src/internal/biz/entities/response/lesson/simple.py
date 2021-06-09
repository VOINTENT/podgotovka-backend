from typing import Optional

from pydantic import Field

from src.internal.biz.entities.response.base import BaseResponseModel
from src.internal.biz.entities.response.course.simple import CourseSimpleResponse
from src.internal.biz.entities.response.subject.simple import SubjectSimpleResponse


class LessonSimpleResponse(BaseResponseModel):
    id: int = Field(..., example=1)
    name: str = Field(..., example='Название')
    course: CourseSimpleResponse
    subject: SubjectSimpleResponse
    start_time: int = Field(..., example=123456789)
    finish_time: Optional[int] = Field(None, example=560)
    is_watched: bool = Field(..., example=True)
