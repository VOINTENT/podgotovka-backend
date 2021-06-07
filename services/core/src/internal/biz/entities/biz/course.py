from typing import Optional


class Course:
    def __init__(self,
                 id: Optional[int] = None,
                 name: Optional[str] = None) -> None:
        self.id = id
        self.name = name
