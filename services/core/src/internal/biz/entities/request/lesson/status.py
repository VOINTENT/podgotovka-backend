from pydantic import Field

from src.internal.biz.entities.enum.lesson_status import LessonStatusEnum
from src.internal.biz.entities.request.base import BaseRequestModel


class LessonStatusUpdateRequest(BaseRequestModel):
    status: LessonStatusEnum = Field(..., example=LessonStatusEnum.published)
