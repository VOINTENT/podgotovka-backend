import datetime
from typing import Optional, List

from src.internal.biz.entities.biz.file import File
from src.internal.biz.entities.biz.homework.homework import Homework


class Lesson:
    def __init__(self,
                 id: Optional[int] = None,
                 name: Optional[str] = None,
                 youtube_link: Optional[str] = None,
                 date_start: Optional[datetime.date] = None,
                 time_start: Optional[datetime.time] = None,
                 time_finish: Optional[datetime.time] = None,
                 description: Optional[str] = None,
                 lecture: Optional[str] = None,
                 subject_id: Optional[int] = None,
                 is_published: Optional[bool] = None,
                 course_id: Optional[int] = None,
                 account_teacher_id: Optional[int] = None,
                 files: List[File] = [],
                 homework: Optional[Homework] = None,
                 ) -> None:
        self.id = id
        self.name = name
        self.youtube_link = youtube_link
        self.description = description
        self.date_start = date_start
        self.time_start = time_start
        self.time_finish = time_finish
        self.course_id = course_id
        self.account_teacher_id = account_teacher_id
        self.subject_id = subject_id
        self.files = files
        self.is_published = is_published
        self.lecture = lecture
        self.homework = homework
