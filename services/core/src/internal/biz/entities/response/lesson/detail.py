from typing import Optional, List

from pydantic import Field

from src.internal.biz.entities.response.homework.homework_info import HomeworkInfoResponse
from src.internal.biz.entities.response.lesson.lesson_file import LessonFileSimpleResponse


class LessonDetailResponse:
    id: int = Field(..., example=1)
    name: str = Field(..., example='Название')
    description: Optional[str] = Field(None, example='Описание')
    files: List[LessonFileSimpleResponse]
    homework: Optional[HomeworkInfoResponse]
    lecture: Optional[str] = Field(None, example='Лекция')
    is_subscribed: bool = Field(..., example=True)
