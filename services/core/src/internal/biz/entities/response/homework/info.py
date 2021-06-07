from typing import Optional

from pydantic import Field

from src.internal.biz.entities.enum.homework_type import HomeworkTypeEnum
from src.internal.biz.entities.response.base import BaseResponseModel


class HomeworkInfoResponse(BaseResponseModel):
    id: int = Field(..., example=1)
    is_available: bool = Field(..., example=True)
    type: HomeworkTypeEnum
    count_questions: Optional[int] = Field(None, example=1)
    count_right_answers: Optional[int] = Field(None, example=5)
