from typing import Optional, List

from pydantic.fields import Field

from src.internal.biz.entities.response.base import BaseResponseModel
from src.internal.biz.entities.response.course.simple import CourseSimpleResponse
from src.internal.biz.entities.response.homework.detail import HomeworkDetailResponse
from src.internal.biz.entities.response.subject.simple import SubjectSimpleResponse


class LessonDetailResponse(BaseResponseModel):
    subject: Optional[SubjectSimpleResponse] = Field(None)
    course: Optional[CourseSimpleResponse] = Field(None)
    name: Optional[str] = Field(None, example='Название')
    description: Optional[str] = Field(None, example='Описание')
    youtube_link: Optional[str] = Field(None, example='https://...')
    date: Optional[int] = Field(None, example=123456789)
    time_start: Optional[int] = Field(None, example=400)
    time_finish: Optional[int] = Field(None, example=460)
    file_links: Optional[List[str]] = Field(None, example=['https://...', 'https://...'])
    lecture: Optional[str] = Field(None, example='Лекция')
    homework: Optional[HomeworkDetailResponse]
