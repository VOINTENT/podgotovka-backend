from typing import List

from src.internal.biz.creators.base import Creator
from src.internal.biz.entities.biz.homework.prompt import Prompt
from src.internal.biz.entities.response.prompt.simple import PromptSimpleResponse


class PromptSimpleResponseCreator(Creator):
    @classmethod
    def get_many_from_prompts(cls, prompts: List[Prompt]) -> List[PromptSimpleResponse]:
        return [cls.get_from_prompt(prompt) for prompt in prompts]

    @staticmethod
    def get_from_prompt(prompt: Prompt) -> PromptSimpleResponse:
        return PromptSimpleResponse(
            text=prompt.text
        )
