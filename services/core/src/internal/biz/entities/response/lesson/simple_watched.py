from pydantic import Field

from src.internal.biz.entities.response.lesson.simple import LessonSimpleResponse


class LessonSimpleWatchedResponse(LessonSimpleResponse):
    is_watched: bool = Field(..., example=True)
