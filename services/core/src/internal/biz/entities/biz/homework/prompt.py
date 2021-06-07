from typing import Optional

from pydantic import Field


class Prompt:
    text: Optional[str] = Field(..., example='Текст в формате JSON')
