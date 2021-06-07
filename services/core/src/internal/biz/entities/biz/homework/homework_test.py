from typing import Optional, List

from src.internal.biz.entities.biz.homework.homework_test_question import HomeworkTestQuestion


class HomeworkTest:
    def __init__(self,
                 id: Optional[int] = None,
                 test_questions: Optional[List[HomeworkTestQuestion]] = None,
                 ) -> None:
        self.id = id
        self.test_questions = test_questions
