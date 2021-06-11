from typing import List

from src.internal.biz.entities.response.base import BaseResponseModel

from pydantic import Field

from src.internal.biz.entities.response.lesson.simple_watched import LessonSimpleWatchedResponse


class LessonSimpleWatchedListWithCountsResponse(BaseResponseModel):
    count_last: int = Field(..., example=10)
    count_next: int = Field(..., example=10)
    lessons: List[LessonSimpleWatchedResponse]
