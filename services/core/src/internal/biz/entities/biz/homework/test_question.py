from typing import Optional, List

from src.internal.biz.entities.biz.homework.answer_variant import AnswerVariant
from src.internal.biz.entities.biz.homework.prompt import Prompt
from src.internal.biz.entities.enum.answer_type import AnswerTypeEnum


class TestQuestion:
    def __init__(self,
                 text: Optional[str] = None,
                 answer_type: Optional[AnswerTypeEnum] = None,
                 answer_variants: Optional[List[AnswerVariant]] = None,
                 count_attempts: Optional[int] = None,
                 prompts: Optional[List[Prompt]] = None) -> None:
        self.text = text
        self.answer_type = answer_type
        self.answer_variants = answer_variants
        self.count_attempts = count_attempts
        self.prompts = prompts
