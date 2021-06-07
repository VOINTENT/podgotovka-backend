from typing import Optional

from src.internal.biz.entities.biz.homework.homework_test import HomeworkTest
from src.internal.biz.entities.biz.homework.homework_without_answer import HomeworkWithoutAnswer
from src.internal.biz.entities.enum.homework_type import HomeworkTypeEnum


class Homework:
    def __init__(self,
                 id: Optional[int] = None,
                 type: Optional[HomeworkTypeEnum] = None,
                 test: Optional[HomeworkTest] = None,
                 without_answer: Optional[HomeworkWithoutAnswer] = None,
                 ) -> None:
        self.id = id
        self.type = type
        self.test = test
        self.without_answer = without_answer
