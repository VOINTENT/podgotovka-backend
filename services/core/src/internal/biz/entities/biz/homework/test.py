from typing import List, Optional

from src.internal.biz.entities.biz.homework.test_question import TestQuestion


class HomeworkTest:
    def __init__(self, test_questions: Optional[List[TestQuestion]] = None) -> None:
        self.test_questions = test_questions
