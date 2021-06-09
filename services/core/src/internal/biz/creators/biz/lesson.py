from asyncpg import Record

from src.internal.biz.creators.biz.base import CreatorBiz
from src.internal.biz.creators.biz.course import CourseCreator
from src.internal.biz.entities.biz.course import Course
from src.internal.biz.entities.biz.lesson import Lesson
from src.internal.biz.entities.request.lesson.update import LessonUpdateRequest


class LessonCreator(CreatorBiz):
    def get_from_record(self, record: Record):
        return Lesson(
            id=record.get('lesson_id'),
            name=record.get('name'),
            youtube_link=record.get('youtube_link'),
            time_start=record.get('time_start'),
            time_finish=record.get('time_finish'),
            description=record.get('description'),
            is_published=record.get('is_published'),
            course=CourseCreator.get_from_record(record),
            account_teacher_id=record.get('account_teacher_id'),
            documents=record.get('documents')
        )

    def get_from_request(self, lesson_request: LessonUpdateRequest) -> Lesson:
        pass
