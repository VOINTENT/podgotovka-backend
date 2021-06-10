from typing import List

from src.internal.biz.creators.base import Creator
from src.internal.biz.entities.biz.homework.prompt import Prompt
from src.internal.biz.entities.response.prompt.simple import PromptSimpleResponse


class QuestionPromptResponseCreator(Creator):
    @classmethod
    def get_from_one(cls, prompt_question: Prompt) -> PromptSimpleResponse:
        return PromptSimpleResponse(
            id=prompt_question.id,
            text=prompt_question.text
        )

    @classmethod
    def get_from_many(cls, prompts_question: List[Prompt]) -> List[PromptSimpleResponse]:
        return [cls.get_from_one(prompt_question) for prompt_question in prompts_question]
