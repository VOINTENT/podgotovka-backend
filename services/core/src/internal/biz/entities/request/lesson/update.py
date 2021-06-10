from typing import Optional, List

from pydantic.fields import Field

from src.internal.biz.entities.request.base import BaseRequestModel
from src.internal.biz.entities.request.homeworks.add import HomeworkAddRequest


class LessonUpdateRequest(BaseRequestModel):
    subject_id: Optional[int] = Field(-1, example=1)
    course_id: Optional[int] = Field(-1, example=2)
    name: Optional[str] = Field(None, example='Название')
    description: Optional[str] = Field(None, example='Описание')
    youtube_link: Optional[str] = Field(None, example='https://...')
    date_start: Optional[int] = Field(-1, example=123456789)
    time_start: Optional[int] = Field(-1, example=400)
    time_finish: Optional[int] = Field(-1, example=460)
    file_links: Optional[List[str]] = Field(None, example=['https://...', 'https://...'])
    lecture: Optional[str] = Field(None, example='Лекция')
    homework: Optional[HomeworkAddRequest]
