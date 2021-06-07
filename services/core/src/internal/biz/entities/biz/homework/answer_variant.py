class AnswerVariant:
    def __init__(self, name: str = None, is_right: bool = False) -> None:
        self.is_right = is_right
        self.name = name
