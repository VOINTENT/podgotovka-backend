from typing import Optional

from pydantic import Field

from src.internal.biz.entities.enum.homework_type import HomeworkTypeEnum
from src.internal.biz.entities.request.base import BaseRequestModel
from src.internal.biz.entities.request.homeworks.test.add import HomeworkTestRequest
from src.internal.biz.entities.request.homeworks.without_answer.add import HomeworkWithoutAnswerRequest


class HomeworkAddRequest(BaseRequestModel):
    lesson_id: int = Field(..., example=1)
    homework_type: HomeworkTypeEnum = Field(..., example=HomeworkTypeEnum.test)
    homework_without_answer: Optional[HomeworkWithoutAnswerRequest]
    homework_test: Optional[HomeworkTestRequest]
