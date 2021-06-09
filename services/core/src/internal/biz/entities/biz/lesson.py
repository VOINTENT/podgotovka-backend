import datetime
from typing import Optional

from src.internal.biz.entities.biz.course import Course
from src.internal.biz.entities.biz.document import Document
from src.internal.biz.entities.biz.homework.homework import Homework
from src.internal.biz.entities.biz.subject import Subject


class Lesson:
    def __init__(self,
                 id: Optional[int] = None,
                 created_at: Optional[datetime.datetime] = None,
                 subject: Optional[Subject] = None,
                 course: Optional[Course] = None,
                 name: Optional[str] = None,
                 description: Optional[str] = None,
                 youtube_link: Optional[str] = None,
                 time_start: Optional[datetime.datetime] = None,
                 time_finish: Optional[datetime.time] = None,
                 documents: Optional[Document] = None,
                 lecture: Optional[str] = None,
                 homework: Optional[Homework] = None,
                 is_published: Optional[bool] = None,
                 account_teacher_id: Optional[int] = None,
                 is_watched: Optional[bool] = None) -> None:
        self.is_watched = is_watched
        self.account_teacher_id = account_teacher_id
        self.is_published = is_published
        self.created_at = created_at
        self.id = id
        self.subject = subject
        self.course = course
        self.name = name
        self.description = description
        self.youtube_link = youtube_link
        self.time_start = time_start
        self.time_finish = time_finish
        self.documents = documents
        self.lecture = lecture
        self.homework = homework

    @property
    def finish_time_in_seconds(self) -> int:
        if not self.time_finish:
            raise TypeError

        return self.time_finish.hour * 3600 + self.time_finish.minute * 60
