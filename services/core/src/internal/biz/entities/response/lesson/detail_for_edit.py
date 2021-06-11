from typing import Optional, List

from pydantic import Field

from src.internal.biz.entities.response.base import BaseResponseModel
from src.internal.biz.entities.response.course.simple import CourseSimpleResponse
from src.internal.biz.entities.response.document.simple import DocumentSimpleResponse
from src.internal.biz.entities.response.homework.detail import HomeworkDetailResponse
from src.internal.biz.entities.response.subject.simple import SubjectSimpleResponse


class LessonDetailForEditResponse(BaseResponseModel):
    subject: SubjectSimpleResponse
    course: CourseSimpleResponse
    name: Optional[str] = Field(None, example='Название')
    description: Optional[str] = Field(None, example='Описание')
    youtube_link: Optional[str] = Field(None, example='https://...')
    time_start: Optional[int] = Field(None, example=123456789)
    time_finish: Optional[int] = Field(None, example=460)
    files: List[DocumentSimpleResponse]
    lecture: Optional[str] = Field(None, example='Лекция')
    homework: Optional[HomeworkDetailResponse]
