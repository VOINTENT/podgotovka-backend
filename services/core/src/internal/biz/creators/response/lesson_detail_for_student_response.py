from src.internal.biz.creators.base import Creator
from src.internal.biz.creators.response.homework_info_response import HomeworkInfoResponseCreator
from src.internal.biz.creators.response.lesson_file_simple_response import LessonFileSimpleResponseCreator
from src.internal.biz.entities.biz.lesson import Lesson
from src.internal.biz.entities.response.lesson.detail_for_student import LessonDetailForStudentResponse


class LessonDetailForStudentResponseCreator(Creator):
    @staticmethod
    def get_from_lesson(lesson: Lesson) -> LessonDetailForStudentResponse:
        return LessonDetailForStudentResponse(
            id=lesson.id,
            name=lesson.name,
            description=lesson.description,
            files=LessonFileSimpleResponseCreator.get_many_from_documents(lesson.documents),
            homework=HomeworkInfoResponseCreator.get_from_homework_info(
                lesson.homework_info) if lesson.homework_info else None,
            lecture=lesson.lecture,
            is_subscribed=lesson.is_subscribed
        )
