import datetime
from typing import Optional

from asyncpg import Record

from src.internal.biz.creators.biz.base import CreatorBiz
from src.internal.biz.creators.biz.file import DocumentCreator
from src.internal.biz.creators.biz.course import CourseCreator
from src.internal.biz.creators.biz.homework.info import HomeworkInfoCreator
from src.internal.biz.creators.biz.subject import SubjectCreator
from src.internal.biz.entities.biz.course import Course
from src.internal.biz.entities.biz.lesson import Lesson
from src.internal.biz.entities.biz.subject import Subject
from src.internal.biz.entities.enum.lesson_status import LessonStatusEnum
from src.internal.biz.entities.request.lesson.update import LessonUpdateRequest


class LessonCreator(CreatorBiz):
    @staticmethod
    def get_from_record(record: Record):
        course = CourseCreator.get_from_record(record) if record.get('course_id') else None
        subject = SubjectCreator.get_from_record(record) if record.get('subject_id') else None
        return Lesson(
            id=record.get('lesson_id'),
            name=record.get('lesson_name'),
            created_at=record.get('lesson_created_at'),
            youtube_link=record.get('lesson_youtube_link'),
            datetime_start=record.get('lesson_datetime_start'),
            time_finish=record.get('lesson_time_finish'),
            description=record.get('lesson_description'),
            status=record.get('lesson_status'),
            account_teacher_id=record.get('account_teacher_id'),
            lecture=record.get('lesson_lecture'),
            course=course,
            subject=subject,
            is_watched=record.get('lesson_is_watched'),
            homework_info=HomeworkInfoCreator.get_from_record(record),
            is_subscribed=record.get('lesson_is_subscribed')
        )

    @classmethod
    def get_from_existed_and_updated(cls, existed_lesson: Lesson, updated_lesson: LessonUpdateRequest) -> Lesson:
        return Lesson(
            subject=None if updated_lesson.subject_id == -1 else Subject(id=existed_lesson.subject.id)
            if updated_lesson.subject_id is None else Subject(id=updated_lesson.subject_id),

            course=None if updated_lesson.course_id == -1 else Course(id=existed_lesson.course.id)
            if updated_lesson.course_id is None else Course(id=updated_lesson.course_id),

            datetime_start=None if updated_lesson.time_start == -1 else existed_lesson.datetime_start
            if updated_lesson.time_start is None else cls._to_datetime_from_sec(updated_lesson.time_start),

            time_finish=None if updated_lesson.time_finish == -1 else existed_lesson.time_finish
            if updated_lesson.time_finish is None else cls._to_time_from_sec(updated_lesson.time_finish),

            documents=None if updated_lesson.files == [] else existed_lesson.documents
            if updated_lesson.files is None else DocumentCreator.get_many_from_document_add_request(
                updated_lesson.files),

            name=cls._get_str_value(existed_lesson.name, updated_lesson.name),
            description=cls._get_str_value(existed_lesson.description, updated_lesson.description),
            youtube_link=cls._get_str_value(existed_lesson.youtube_link, updated_lesson.youtube_link),
            lecture=cls._get_str_value(existed_lesson.lecture, updated_lesson.lecture)
        )

    @staticmethod
    def _get_int_value(existed_value: Optional[int], updated_value: Optional[int]) -> Optional[int]:
        return None if updated_value == -1 else existed_value if updated_value is None else updated_value

    @staticmethod
    def _get_str_value(existed_value: Optional[str], updated_value: Optional[str]) -> Optional[str]:
        return None if updated_value == '' else existed_value if updated_value is None else updated_value

    @classmethod
    def get_empty(cls, account_teacher_id: int) -> Lesson:
        return Lesson(account_teacher_id=account_teacher_id, status=LessonStatusEnum.draft)

    @staticmethod
    def _to_datetime_from_sec(sec: Optional[int]) -> Optional[datetime.datetime]:
        if sec is None:
            return None
        elif sec == -1:
            return
        return datetime.datetime.fromtimestamp(sec)

    @staticmethod
    def _to_time_from_sec(sec: int) -> datetime.time:
        return datetime.time(
            hour=sec // 3600,
            minute=(sec % 3600) // 60
        )
