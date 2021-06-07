from typing import Optional


class HomeworkWithoutAnswer:
    def __init__(self,
                 id: Optional[int] = None,
                 question: Optional[str] = None,
                 ) -> None:
        self.id = id
        self.question = question
