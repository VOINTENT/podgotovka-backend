from typing import Optional, List

from src.internal.biz.entities.biz.homework.homework_test_question_prompt import HomeworkTestQuestionPrompt
from src.internal.biz.entities.enum.answer_type import AnswerTypeEnum


class HomeworkTestQuestion:
    def __init__(self,
                 id: Optional[int] = None,
                 name: Optional[str] = None,
                 description: Optional[dict] = None,
                 answer_type: Optional[AnswerTypeEnum] = None,
                 count_attempts: Optional[int] = None,
                 homework_test_id: Optional[int] = None,
                 prompts: Optional[List[HomeworkTestQuestionPrompt]] = None,
                 ) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.answer_type = answer_type
        self.count_attempts = count_attempts
        self.homework_test_id = homework_test_id
        self.prompts = prompts
