import datetime

from asyncpg import Record

from src.internal.biz.creators.biz.base import CreatorBiz
from src.internal.biz.creators.biz.file import DocumentCreator
from src.internal.biz.creators.biz.homework.homework import HomeworkCreator
from src.internal.biz.creators.biz.course import CourseCreator
from src.internal.biz.creators.biz.homework.info import HomeworkInfoCreator
from src.internal.biz.creators.biz.subject import SubjectCreator
from src.internal.biz.entities.biz.lesson import Lesson
from src.internal.biz.entities.request.lesson.update import LessonUpdateRequest


class LessonCreator(CreatorBiz):
    @staticmethod
    def get_from_record(record: Record):
        course = CourseCreator.get_from_record(record)
        subject = SubjectCreator.get_from_record(record)
        return Lesson(
            id=record.get('lesson_id'),
            name=record.get('lesson_name'),
            created_at=record.get('lesson_created_at'),
            youtube_link=record.get('lesson_youtube_link'),
            datetime_start=record.get('lesson_datetime_start'),
            time_finish=record.get('lesson_time_finish'),
            description=record.get('lesson_description'),
            is_published=record.get('lesson_is_published'),
            account_teacher_id=record.get('account_teacher_id'),
            lecture=record.get('lesson_lecture'),
            course=course,
            subject=subject,
            is_watched=record.get('lesson_is_watched'),
            homework_info=HomeworkInfoCreator.get_from_record(record),
            is_subscribed=record.get('lesson_is_subscribed')
        )

    @classmethod
    def get_from_request(cls, lesson_request: LessonUpdateRequest,
                         lesson_id: int,
                         account_teacher_id: int) -> Lesson:
        lesson = Lesson()

        if lesson_request.homework:
            lesson.homework = HomeworkCreator().get_from_request(lesson_request.homework)
        if lesson_request.file_links:
            lesson.documents = [DocumentCreator().get_from_requests(link) for link in lesson_request.file_links]

        lesson.id = lesson_id
        lesson.account_teacher_id = account_teacher_id

        if lesson_request.name is not None:
            lesson.name = lesson_request.name

        if lesson_request.description is not None:
            lesson.description = lesson_request.description

        if lesson_request.youtube_link is not None:
            lesson.youtube_link = lesson_request.youtube_link

        if lesson_request.lecture is not None:
            lesson.lecture = lesson_request.lecture

        if lesson_request.course_id != -1:
            lesson.course = CourseCreator.get_from_request(lesson_request.course_id)

        if lesson_request.subject_id != -1:
            lesson.subject = SubjectCreator.get_from_request(lesson_request.subject_id)

        if lesson_request.date_start != -1:
            lesson.datetime_start = cls._to_date_from_sec(lesson_request.date_start)

        if lesson_request.time_finish != -1:
            lesson.time_finish = cls._to_time_from_sec(lesson_request.time_finish)
        return lesson

    @staticmethod
    def _to_date_from_sec(sec: int) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(sec)

    @staticmethod
    def _to_time_from_sec(sec: int) -> datetime.time:
        return datetime.time(
            hour=sec // 3600,
            minute=(sec % 3600) // 60
        )
