from asyncpg import Record

from src.internal.biz.creators.biz.base import CreatorBiz
from src.internal.biz.entities.biz.homework.prompt import Prompt
from src.internal.biz.entities.request.homeworks.test.question.prompt.add import PromptRequest


class PromptCreator(CreatorBiz):
    def get_from_request(self, prompt_request: PromptRequest) -> Prompt:
        return Prompt(text=prompt_request.text)

    @staticmethod
    def get_from_record(record: Record):
        return Prompt(id=record.get('prompt_id'),
                      text=record.get('prompt_text'))
