import datetime
from typing import Optional, List

from src.internal.biz.entities.biz.course import Course
from src.internal.biz.entities.biz.document import Document
from src.internal.biz.entities.biz.homework.homework import Homework
from src.internal.biz.entities.biz.homework.info import HomeworkInfo
from src.internal.biz.entities.biz.subject import Subject
from src.internal.biz.entities.enum.lesson_status import LessonStatusEnum
from src.internal.servers.http.exceptions.lesson import LessonExceptionEnum


class Lesson:
    def __init__(self,
                 id: Optional[int] = None,
                 created_at: Optional[datetime.datetime] = None,
                 subject: Optional[Subject] = None,
                 course: Optional[Course] = None,
                 name: Optional[str] = None,
                 description: Optional[str] = None,
                 youtube_link: Optional[str] = None,
                 datetime_start: Optional[datetime.datetime] = None,
                 time_finish: Optional[datetime.time] = None,
                 documents: Optional[List[Document]] = None,
                 lecture: Optional[str] = None,
                 homework: Optional[Homework] = None,
                 status: Optional[LessonStatusEnum] = None,
                 account_teacher_id: Optional[int] = None,
                 is_watched: Optional[bool] = None,
                 is_subscribed: Optional[bool] = None,
                 homework_info: Optional[HomeworkInfo] = None) -> None:
        self.homework_info = homework_info
        self.is_subscribed = is_subscribed
        self.is_watched = is_watched
        self.account_teacher_id = account_teacher_id
        self.status = status
        self.created_at = created_at
        self.id = id
        self.lecture = lecture
        self.datetime_start = datetime_start
        self.subject = subject
        self.course = course
        self.name = name
        self.description = description
        self.youtube_link = youtube_link
        self.time_finish = time_finish
        self.documents = documents
        self.homework = homework
        self.account_teacher_id = account_teacher_id

    @property
    def datetime_start_timestamp(self) -> Optional[int]:
        if not self.datetime_start:
            return None
        return int(self.datetime_start.timestamp())

    @property
    def finish_time_in_seconds(self) -> Optional[int]:
        if not self.time_finish:
            return None

        return self.time_finish.hour * 3600 + self.time_finish.minute * 60

    def validate(self) -> None:
        if not self.subject:
            raise LessonExceptionEnum.LESSON_NOT_SUBJECT

        if not self.course:
            raise LessonExceptionEnum.LESSON_NOT_COURSE

        if not self.name:
            raise LessonExceptionEnum.LESSON_NOT_NAME

        if not self.youtube_link:
            raise LessonExceptionEnum.LESSON_NOT_YOUTUBE_LINK

        if not self.datetime_start:
            raise LessonExceptionEnum.LESSON_NOT_DATETIME_START
