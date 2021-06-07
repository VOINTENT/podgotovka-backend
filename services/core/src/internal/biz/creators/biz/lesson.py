from asyncpg import Record

from src.internal.biz.creators.biz.base import CreatorBiz
from src.internal.biz.entities.biz.lesson import Lesson
from src.internal.biz.entities.request.lesson.update import LessonUpdateRequest


class LessonCreator(CreatorBiz):
    def get_from_record(self, record: Record):
        return Lesson(
            id=record.get('lesson_id'),
            name=record.get('name'),
            youtube_link=record.get('youtube_link'),
            date_start=record.get('date_start'),
            time_start=record.get('time_start'),
            time_finish=record.get('time_finish'),
            description=record.get('description'),
            is_published=record.get('is_published'),
            course_id=record.get('course_id'),
            account_teacher_id=record.get('account_teacher_id'),
            files=record.get('files')
        )

    def get_from_request(self, lesson_request: LessonUpdateRequest) -> Lesson:
        pass
