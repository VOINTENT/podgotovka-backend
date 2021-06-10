from typing import Optional


class AnswerVariant:
    def __init__(self,
                 id: Optional[int] = None,
                 name: str = None,
                 is_right: bool = False) -> None:
        self.id = id
        self.is_right = is_right
        self.name = name
