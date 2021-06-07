from typing import Optional

from pydantic import Field

from src.internal.biz.entities.enum.homework_type import HomeworkTypeEnum
from src.internal.biz.entities.response.base import BaseResponseModel
from src.internal.biz.entities.response.homework.test_detail_with_results import HomeworkTestDetailWithResultsResponse
from src.internal.biz.entities.response.homework.without_answer_detail import HomeworkWithoutAnswerDetailResponse


class HomeworkDetailWithResultsResponse(BaseResponseModel):
    id: int = Field(..., example=1)
    type: HomeworkTypeEnum
    homework_without_answer: Optional[HomeworkWithoutAnswerDetailResponse]
    homework_test: Optional[HomeworkTestDetailWithResultsResponse]
