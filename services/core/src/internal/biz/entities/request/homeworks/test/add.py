from typing import List

from src.internal.biz.entities.request.base import BaseRequestModel
from src.internal.biz.entities.request.homeworks.test.question.add import TestQuestionRequest


class HomeworkTestRequest(BaseRequestModel):
    test_questions: List[TestQuestionRequest]
