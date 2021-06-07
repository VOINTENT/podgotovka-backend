from typing import Optional

from src.internal.biz.entities.biz.homework.test import HomeworkTest
from src.internal.biz.entities.biz.homework.without_answer import HomeworkWithoutAnswer
from src.internal.biz.entities.enum.homework_type import HomeworkTypeEnum


class Homework:
    def __init__(self,
                 homework_type: Optional[HomeworkTypeEnum] = None,
                 without_answer: Optional[HomeworkWithoutAnswer] = None,
                 homework_test: Optional[HomeworkTest] = None) -> None:
        self.homework_type = homework_type
        self.without_answer = without_answer
        self.homework_test = homework_test
