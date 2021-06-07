from typing import Optional


class HomeworkTestQuestionPrompt:
    def __init__(self,
                 id: Optional[int] = None,
                 test_question_id: Optional[int] = None,
                 text: Optional[dict] = None,
                 ) -> None:
        self.id = id
        self.test_question_id = test_question_id
        self.text = text
