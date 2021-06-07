import datetime
from typing import Optional

from src.internal.biz.entities.biz.course import Course
from src.internal.biz.entities.biz.document import Document
from src.internal.biz.entities.biz.homework.homework import Homework
from src.internal.biz.entities.biz.subject import Subject


class Lesson:
    def __init__(self,
                 subject: Optional[Subject] = None,
                 course: Optional[Course] = None,
                 name: Optional[str] = None,
                 description: Optional[str] = None,
                 youtube_link: Optional[str] = None,
                 time_start: Optional[datetime.datetime] = None,
                 time_finish: Optional[datetime.time] = None,
                 documents: Optional[Document] = None,
                 lecture: Optional[str] = None,
                 homework: Optional[Homework] = None) -> None:
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
