from typing import Optional


class Subject:
    def __init__(self,
                 id: Optional[int],
                 name: Optional[str]) -> None:
        self.name = name
        self.id = id
