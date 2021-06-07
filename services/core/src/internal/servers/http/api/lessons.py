from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends

from src.internal.biz.creators.response.lesson import LessonResponseCreator
from src.internal.biz.entities.biz.account.account_student import AccountStudent
from src.internal.biz.entities.biz.account.account_teacher import AccountTeacher
from src.internal.biz.entities.enum.order import OrderEnum
from src.internal.biz.entities.request.lesson.update import LessonUpdateRequest
from src.internal.biz.entities.response.lesson.detail import LessonDetailResponse
from src.internal.biz.entities.response.lesson.detail_for_student import LessonDetailForStudentResponse
from src.internal.biz.entities.response.lesson.simple_with_counts import LessonSimpleListWithCountsResponse
from src.internal.biz.services.lesson import LessonService
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
    lessons_with_counts = await LessonService.get_all_lessons_with_counts(
        limit=pagination_params.limit, skip=pagination_params.skip, date_start=date_start, order=order,
        course_id=course_id, subject_id=subject_id)
    return LessonSimpleResponseCreator.get_from_lesson_with_counts_many(lessons_with_counts)


@lessons_router.get('/my/teachers', response_model=LessonSimpleListWithCountsResponse)
async def get_my_teacher_lessons(
        account_teacher: AccountTeacher = Depends(get_current_account_teacher),
        date_start: datetime = Depends(get_date_start),
        pagination_params: PaginationParams = Depends(),
        order: OrderEnum = Depends(get_order),
        course_id: int = Depends(get_course_id),
        subject_id: int = Depends(get_subject_id)):
    pass


@lessons_router.get('/my/students', response_model=LessonSimpleListWithCountsResponse)
async def get_my_student_lessons(
        account_student: AccountStudent = Depends(get_current_account_student),
        date_start: datetime = Depends(get_date_start),
        pagination_params: PaginationParams = Depends(),
        order: OrderEnum = Depends(get_order),
        course_id: int = Depends(get_course_id),
        subject_id: int = Depends(get_subject_id)
):
    pass


@lessons_router.get('/{lesson_id}', response_model=LessonDetailForStudentResponse)
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


@lessons_router.post('/', response_model=LessonDetailResponse)
async def lesson_create(account_teacher_request: AccountTeacher = Depends(get_current_account_teacher)):
    lesson = await LessonService.create_empty_lesson(account_teacher_request.id)
    return LessonResponseCreator.get_detail_from_lesson(lesson)


@lessons_router.patch('/{lesson_id}', response_model=LessonDetailResponse)
async def lesson_update(lesson_id: int, lesson_request: LessonUpdateRequest,
                        account_teacher_request: AccountTeacher = Depends(get_current_account_teacher)):
    pass
