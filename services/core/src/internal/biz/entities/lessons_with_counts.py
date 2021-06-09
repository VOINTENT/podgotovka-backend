from typing import List

from src.internal.biz.entities.biz.lesson import Lesson


class LessonsWithCounts:
    def __init__(self, lessons: List[Lesson], count_last: int, count_next: int) -> None:
        self.count_next = count_next
        self.count_last = count_last
        self.lessons = lessons
