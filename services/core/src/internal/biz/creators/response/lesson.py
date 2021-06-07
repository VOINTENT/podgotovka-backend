from src.internal.biz.entities.biz.lesson import Lesson
from src.internal.biz.entities.response.lesson.detail import LessonDetailResponse
from src.internal.biz.entities.response.lesson.simple import LessonSimpleResponse


class LessonResponseCreator:
    @staticmethod
    def get_detail_from_lesson(lesson: Lesson) -> LessonDetailResponse:
        return LessonDetailResponse(
            subject=lesson.subject_id,
            course=lesson.course_id,
            name=lesson.name,
            description=lesson.description,
            youtube_link=lesson.youtube_link,
            date=lesson.date_start,
            time_start=lesson.time_start,
            time_finish=lesson.time_finish,
            lecture=lesson.lecture,
            # homework=lesson.homework,
        )

    @staticmethod
    def get_simple_from_lesson(lesson: Lesson) -> LessonSimpleResponse:
        return LessonSimpleResponse(
        )
