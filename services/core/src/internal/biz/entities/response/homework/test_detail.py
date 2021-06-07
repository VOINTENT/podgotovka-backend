from typing import List

from src.internal.biz.entities.response.base import BaseResponseModel
from src.internal.biz.entities.response.test_question.detail import TestQuestionDetailResponse


class HomeworkTestDetailResponse(BaseResponseModel):
    test_questions: List[TestQuestionDetailResponse]
