from typing import Optional


class Prompt:
    def __init__(self, id: Optional[int] = None,
                 text: Optional[str] = None) -> None:
        self.id = id
        self.text = text
