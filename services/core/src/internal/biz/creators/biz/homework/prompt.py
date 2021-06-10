from typing import Dict, Any, List

from asyncpg import Record

from src.internal.biz.creators.biz.base import CreatorBiz
from src.internal.biz.entities.biz.homework.prompt import Prompt
from src.internal.biz.entities.request.homeworks.test.question.prompt.add import PromptRequest


class PromptCreator(CreatorBiz):
    @staticmethod
    def get_from_request(prompt_request: PromptRequest) -> Prompt:
        return Prompt(text=prompt_request.text)

    @staticmethod
    def get_from_record(record: Record):
        return Prompt(id=record.get('prompt_id'),
                      text=record.get('prompt_text'))

    @classmethod
    def get_many_from_dicts(cls, prompts: List[Dict[str, Any]]) -> List[Prompt]:
        return [cls.get_from_dict(prompt) for prompt in prompts]

    @staticmethod
    def get_from_dict(prompt: Dict[str, Any]) -> Prompt:
        return Prompt(
            text=prompt.get('prompt_text')
        )
