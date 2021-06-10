from typing import Optional

from pydantic import Field


class Prompt:

    def __init__(self, text: str) -> None:
        self.text = text
