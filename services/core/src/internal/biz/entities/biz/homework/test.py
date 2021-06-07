from typing import List, Optional


class HomeworkTest:
    def __init__(self, test_questions: Optional[List[TestQuestion]] = None) -> None:
        self.test_questions = test_questions
