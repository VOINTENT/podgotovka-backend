from typing import Optional

from fastapi import APIRouter, Depends

from src.internal.biz.creators.response.homework_detail_with_results import HomeworkDetailWithResultsResponseCreator
from src.internal.biz.entities.biz.account.account_student import AccountStudent
from src.internal.biz.entities.request.test_question.answer import TestQuestionAnswerRequest
from src.internal.biz.entities.response.homework.detail_with_results import HomeworkDetailWithResultsResponse
from src.internal.biz.entities.response.test_question.result.after_answer import TestQuestionResultAfterAnswerResponse
from src.internal.biz.entities.response.test_question.result.after_reject import TestQuestionResultAfterRejectResponse
from src.internal.biz.services.homework import HomeworkService
from src.internal.servers.http.depends.auth import get_optional_current_account_student

homeworks_router = APIRouter(prefix='/homeworks', tags=['Homeworks'])


@homeworks_router.get('/{homework_id}/students', response_model=HomeworkDetailWithResultsResponse)
async def get_homework_detail_for_student(
        homework_id: int,
        current_account_student: Optional[AccountStudent] = Depends(get_optional_current_account_student)):
    homework = await HomeworkService.get_homework_detail_for_student(
        homework_id, current_account_student.id if current_account_student else None)
    return HomeworkDetailWithResultsResponseCreator.get_from_homework(homework)


@homeworks_router.post('/questions/{question_id}/answer', response_model=TestQuestionResultAfterAnswerResponse)
async def answer_on_question(
        question_id: int, question_answer_request: TestQuestionAnswerRequest,
        current_account_student: Optional[AccountStudent] = Depends(get_optional_current_account_student)):
    pass


@homeworks_router.post('/questions/{question_id}/reject', response_model=TestQuestionResultAfterRejectResponse)
async def reject_on_question(
        question_id: int,
        current_account_student: Optional[AccountStudent] = Depends(get_optional_current_account_student)):
    pass
