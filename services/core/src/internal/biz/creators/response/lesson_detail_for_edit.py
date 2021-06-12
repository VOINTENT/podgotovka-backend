from src.internal.biz.creators.base import Creator
from src.internal.biz.creators.response.course_simple import CourseSimpleResponseCreator
from src.internal.biz.creators.response.document_simple import DocumentSimpleResponseCreator
from src.internal.biz.creators.response.subject_simple import SubjectSimpleResponseCreator
from src.internal.biz.entities.biz.lesson import Lesson
from src.internal.biz.entities.response.lesson.detail_for_edit import LessonDetailForEditResponse


class LessonDetailForEditResponseCreator(Creator):
    @staticmethod
    def get_from_lesson(lesson: Lesson) -> LessonDetailForEditResponse:
        return LessonDetailForEditResponse(
            id=lesson.id,
            subject=SubjectSimpleResponseCreator.get_from_subject(lesson.subject) if lesson.subject else None,
            course=CourseSimpleResponseCreator.get_from_course(lesson.course) if lesson.course else None,
            name=lesson.name,
            description=lesson.description,
            youtube_link=lesson.youtube_link,
            time_start=lesson.datetime_start_timestamp,
            time_finish=lesson.finish_time_in_seconds,
            files=DocumentSimpleResponseCreator.get_many_from_documents(lesson.documents) if lesson.documents else [],
            lecture=lesson.lecture,
            status=lesson.status
        )
