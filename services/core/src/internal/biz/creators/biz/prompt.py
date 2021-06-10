from typing import Dict, List, Any

from src.internal.biz.creators.base import Creator
from src.internal.biz.entities.biz.homework.prompt import Prompt


class PromptCreator(Creator):
    @classmethod
    def get_many_from_dicts(cls, prompts: List[Dict[str, Any]]) -> List[Prompt]:
        return [cls.get_from_dict(prompt) for prompt in prompts]

    @staticmethod
    def get_from_dict(prompt: Dict[str, Any]) -> Prompt:
        return Prompt(
            text=prompt.get('prompt_text')
        )
