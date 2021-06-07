from typing import List, Optional

from pydantic import Field

from src.internal.biz.entities.request.base import BaseRequestModel


class LessonAddRequest(BaseRequestModel):
    subject_id: int = Field(..., example=1)
    course_id: int = Field(..., example=2)
    name: str = Field(..., example='Название')
    description: Optional[str] = Field(None, example='Описание')
    youtube_link: str = Field(..., example='https://...')
    date: int = Field(..., example=123456789)
    time_start: int = Field(..., example=400)
    time_finish: int = Field(..., example=460)
    file_links: Optional[List[str]] = Field([], example=['https://...', 'https://...'])
    lecture: Optional[str] = Field(None, example='Лекция')
    is_published: Optional[bool] = Field(False, example=False)
