from typing import List

from src.internal.biz.entities.response.base import BaseResponseModel
from src.internal.biz.entities.response.test_question.detail_with_result import TestQuestionDetailWithResultResponse


class HomeworkTestDetailWithResultsResponse(BaseResponseModel):
    test_questions: List[TestQuestionDetailWithResultResponse]
