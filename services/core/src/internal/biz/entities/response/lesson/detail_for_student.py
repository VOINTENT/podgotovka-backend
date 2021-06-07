from typing import Optional, List

from pydantic import Field

from src.internal.biz.entities.response.base import BaseResponseModel
from src.internal.biz.entities.response.homework.info import HomeworkInfoResponse
from src.internal.biz.entities.response.lesson.lesson_file import LessonFileSimpleResponse


class LessonDetailForStudentResponse(BaseResponseModel):
    id: int = Field(..., example=1)
    name: str = Field(..., example='Название')
    description: Optional[str] = Field(None, example='Описание')
    files: List[LessonFileSimpleResponse]
    homework: Optional[HomeworkInfoResponse]
    lecture: Optional[str] = Field(None, example='Лекция')
    is_subscribed: Optional[bool] = Field(None, example=True)
