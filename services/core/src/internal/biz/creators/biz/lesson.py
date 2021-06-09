from typing import List

from asyncpg import Record

from src.internal.biz.creators.biz.base import CreatorBiz
from src.internal.biz.creators.biz.course import CourseCreator
from src.internal.biz.creators.biz.homework_info import HomeworkInfoCreator
from src.internal.biz.creators.biz.subject import SubjectCreator
from src.internal.biz.entities.biz.lesson import Lesson
from src.internal.biz.entities.request.lesson.update import LessonUpdateRequest


class LessonCreator(CreatorBiz):
    @staticmethod
    def get_from_record(record: Record):
        return Lesson(
            id=record.get('lesson_id'),
            created_at=record.get('lesson_created_at'),
            name=record.get('lesson_name'),
            youtube_link=record.get('lesson_youtube_link'),
            time_start=record.get('lesson_time_start'),
            time_finish=record.get('lesson_time_finish'),
            description=record.get('lesson_description'),
            is_published=record.get('lesson_is_published'),
            course=CourseCreator.get_from_record(record),
            subject=SubjectCreator.get_from_record(record),
            account_teacher_id=record.get('account_teacher_id'),
            is_watched=record.get('lesson_is_watched'),
            lecture=record.get('lesson_lecture'),
            homework_info=HomeworkInfoCreator.get_from_record(record),
            is_subscribed=record.get('lesson_is_subscribed')
        )

    @classmethod
    def get_from_record_many(cls, records: List[Record]):
        return super().get_from_record_many(records)

    @staticmethod
    def get_from_request(lesson_request: LessonUpdateRequest) -> Lesson:
        pass
