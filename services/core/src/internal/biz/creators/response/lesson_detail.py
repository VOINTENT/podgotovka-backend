import datetime
from typing import List, Optional

from src.internal.biz.creators.base import Creator
from src.internal.biz.creators.response.course_simple import CourseSimpleResponseCreator
from src.internal.biz.creators.response.homework.homework_detail import HomeworkDetailResponseCreator
from src.internal.biz.creators.response.lesson_file_simple import LessonFileSimpleResponseCreator
from src.internal.biz.creators.response.subject_simple import SubjectSimpleResponseCreator
from src.internal.biz.entities.biz.lesson import Lesson
from src.internal.biz.entities.response.lesson.detail import LessonDetailResponse


class LessonDetailResponseCreator(Creator):
    @classmethod
    def get_from_one(cls, lesson: Lesson) -> LessonDetailResponse:
        homework = HomeworkDetailResponseCreator().get_from_one(lesson.homework) if lesson.homework else None
        subject = SubjectSimpleResponseCreator.get_from_subject(lesson.subject) if lesson.subject else None
        course = CourseSimpleResponseCreator.get_from_course(lesson.course) if lesson.course else None
        file_links = LessonFileSimpleResponseCreator.get_from_many(lesson.documents) if lesson.documents else []
        return LessonDetailResponse(
            id=lesson.id,
            subject=subject,
            course=course,
            name=lesson.name,
            description=lesson.description,
            youtube_link=lesson.youtube_link,
            date=cls.to_sec_from_date(lesson.datetime_start),
            time_finish=cls.to_sec_from_time(lesson.time_finish),
            lecture=lesson.lecture,
            homework=homework,
            is_published=lesson.is_published,
            file_links=file_links
        )

    @classmethod
    def get_from_many(cls, lessons: List[Lesson]) -> List[LessonDetailResponse]:
        return [cls.get_from_one(lesson) for lesson in lessons]

    @staticmethod
    def to_sec_from_date(date: datetime.datetime) -> Optional[int]:
        if date:
            return int(date.timestamp())
        return None

    @staticmethod
    def to_sec_from_time(time: datetime.datetime.time) -> Optional[int]:
        if time:
            return (time.hour * 3600) + (time.minute * 60)
        return None
