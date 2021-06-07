from typing import Optional


class Subject:
    def __init__(self,
                 id: Optional[int] = None,
                 name: Optional[str] = None) -> None:
        self.name = name
        self.id = id
