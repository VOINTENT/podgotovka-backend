from typing import Optional


class AnswerVariant:
    def __init__(self, id: Optional[int], name: Optional[str] = None, is_right: Optional[bool] = False) -> None:
        self.id = id
        self.is_right = is_right
        self.name = name
