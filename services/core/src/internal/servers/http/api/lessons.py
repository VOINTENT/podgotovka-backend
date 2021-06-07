from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends

from src.internal.biz.entities.biz.account.account_student import AccountStudent
from src.internal.biz.entities.biz.account.account_teacher import AccountTeacher
from src.internal.biz.entities.enum.order import OrderEnum
from src.internal.biz.entities.request.lesson.add import LessonAddRequest
from src.internal.biz.entities.response.lesson.detail import LessonDetailResponse
from src.internal.biz.entities.response.lesson.simple_with_counts import LessonSimpleListWithCountsResponse
from src.internal.servers.http.depends.auth import get_current_account_student, get_optional_current_account_student, \
    get_current_account_teacher
from src.internal.servers.http.depends.filters import get_date_start, get_order, get_course_id, get_subject_id
from src.internal.servers.http.depends.pagination import PaginationParams

lessons_router = APIRouter(prefix='/lessons', tags=['Lessons'])


@lessons_router.get('/', response_model=LessonSimpleListWithCountsResponse)
async def get_lessons(date_start: datetime = Depends(get_date_start),
                      pagination_params: PaginationParams = Depends(),
                      order: OrderEnum = Depends(get_order),
                      course_id: int = Depends(get_course_id),
                      subject_id: int = Depends(get_subject_id)):
    pass


@lessons_router.get('/my/teachers', response_model=LessonSimpleListWithCountsResponse)
async def get_my_student_lessons(
        account_student: AccountStudent = Depends(get_current_account_student),
        date_start: datetime = Depends(get_date_start),
        pagination_params: PaginationParams = Depends(),
        order: OrderEnum = Depends(get_order),
        course_id: int = Depends(get_course_id),
        subject_id: int = Depends(get_subject_id)):
    pass


@lessons_router.get('/my/students', response_model=LessonSimpleListWithCountsResponse)
async def get_my_teacher_lessons(
        account_teacher: AccountStudent = Depends(get_current_account_teacher),
        date_start: datetime = Depends(get_date_start),
        pagination_params: PaginationParams = Depends(),
        order: OrderEnum = Depends(get_order),
        course_id: int = Depends(get_course_id),
        subject_id: int = Depends(get_subject_id)
):
    pass


@lessons_router.get('/{lesson_id}', response_model=LessonDetailResponse)
async def get_lesson_detail(
        lesson_id: int,
        current_account_student: Optional[AccountStudent] = Depends(get_optional_current_account_student)):
    pass


@lessons_router.post('/{lesson_id}/watched', response_model=bool)
async def set_lesson_watched(lesson_id: int, account_student: AccountStudent = Depends(get_current_account_student)):
    pass


@lessons_router.post('/{lesson_id}/subscription', response_model=bool)
async def subscribe_to_subject_and_course(lesson_id: int,
                                          account_student: AccountStudent = Depends(get_current_account_student)):
    pass


@lessons_router.delete('/{lesson_id}/subscription', response_model=bool)
async def unsubscribe_to_subject_and_course(lesson_id: int,
                                            account_student: AccountStudent = Depends(get_current_account_student)):
    pass


@lessons_router.post('/')
async def lesson_create(lesson_request: LessonAddRequest,
                        account_teacher_request: AccountTeacher = Depends(get_current_account_teacher)):
    pass
