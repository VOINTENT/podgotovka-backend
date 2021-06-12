from datetime import datetime
from typing import Optional, List

from fastapi import APIRouter, Depends

from src.internal.biz.creators.response.just_id import JustIdResponseCreator
from src.internal.biz.creators.response.lesson_detail_for_edit import LessonDetailForEditResponseCreator
from src.internal.biz.creators.response.lesson_detail_for_student_response import LessonDetailForStudentResponseCreator
from src.internal.biz.creators.response.lesson_only_name import LessonOnlyNameResponseCreator
from src.internal.biz.creators.response.lessons_simple_with_counts import LessonSimpleListWithCountsResponseCreator
from src.internal.biz.entities.biz.account.account_student import AccountStudent
from src.internal.biz.entities.biz.account.account_teacher import AccountTeacher
from src.internal.biz.entities.biz.lesson import Lesson
from src.internal.biz.entities.enum.order import OrderEnum
from src.internal.biz.entities.lessons_with_counts import LessonsWithCounts
from src.internal.biz.entities.request.lesson.status import LessonStatusUpdateRequest
from src.internal.biz.entities.request.lesson.update import LessonUpdateRequest
from src.internal.biz.entities.response.common.just_id import JustIdResponse
from src.internal.biz.entities.response.lesson.detail_for_edit import LessonDetailForEditResponse
from src.internal.biz.entities.response.lesson.detail_for_student import LessonDetailForStudentResponse
from src.internal.biz.entities.response.lesson.only_name import LessonOnlyNameResponse
from src.internal.biz.entities.response.lesson.simple_watched_with_counts import \
    LessonSimpleWatchedListWithCountsResponse
from src.internal.biz.entities.response.lesson.simple_with_counts import LessonSimpleListWithCountsResponse
from src.internal.biz.services.lesson import LessonService
from src.internal.servers.http.depends.auth import get_current_account_student, get_optional_current_account_student, \
    get_current_account_teacher
from src.internal.servers.http.depends.filters import get_date_start, get_order, get_course_id, get_subject_id, \
    get_date_finish
from src.internal.servers.http.depends.pagination import PaginationParams

lessons_router = APIRouter(prefix='/lessons', tags=['Lessons'])


@lessons_router.get('/', response_model=LessonSimpleListWithCountsResponse)
async def get_published_lessons(date_start: datetime = Depends(get_date_start),
                                date_finish: datetime = Depends(get_date_finish),
                                pagination_params: PaginationParams = Depends(),
                                order: OrderEnum = Depends(get_order),
                                course_id: int = Depends(get_course_id),
                                subject_id: int = Depends(get_subject_id)):
    lessons_with_counts: LessonsWithCounts = await LessonService.get_published_lessons_with_counts(
        limit=pagination_params.limit, skip=pagination_params.skip, date_start=date_start, order=order,
        course_id=course_id, subject_id=subject_id, date_finish=date_finish)
    return LessonSimpleListWithCountsResponseCreator.get_from_lessons_with_counts(lessons_with_counts)


@lessons_router.get('/my/teachers', response_model=LessonSimpleListWithCountsResponse)
async def get_my_teacher_lessons(
        account_teacher: AccountTeacher = Depends(get_current_account_teacher),
        date_start: datetime = Depends(get_date_start),
        date_finish: datetime = Depends(get_date_finish),
        pagination_params: PaginationParams = Depends(),
        order: OrderEnum = Depends(get_order),
        course_id: int = Depends(get_course_id),
        subject_id: int = Depends(get_subject_id)):
    lessons_with_counts: LessonsWithCounts = await LessonService.get_lessons_for_teacher(
        account_teacher_id=account_teacher.id, limit=pagination_params.limit, skip=pagination_params.skip,
        date_start=date_start, date_finish=date_finish, order=order, course_id=course_id, subject_id=subject_id)
    return LessonSimpleListWithCountsResponseCreator.get_from_lessons_with_counts(lessons_with_counts)


@lessons_router.get('/my/students', response_model=LessonSimpleWatchedListWithCountsResponse)
async def get_my_student_lessons(
        account_student: AccountStudent = Depends(get_current_account_student),
        date_start: datetime = Depends(get_date_start),
        pagination_params: PaginationParams = Depends(),
        order: OrderEnum = Depends(get_order),
        course_id: int = Depends(get_course_id),
        subject_id: int = Depends(get_subject_id)
):
    pass


@lessons_router.get('/{lesson_id}/students', response_model=LessonDetailForStudentResponse)
async def get_lesson_detail_for_student(
        lesson_id: int,
        current_account_student: Optional[AccountStudent] = Depends(get_optional_current_account_student)):
    lesson = await LessonService.get_lesson_detail_for_student(
        lesson_id, current_account_student.id if current_account_student else None)
    return LessonDetailForStudentResponseCreator.get_from_lesson(lesson)


@lessons_router.get('/{lesson_id}/teachers/for-edit', response_model=LessonDetailForEditResponse)
async def get_lesson_detail_for_edit(lesson_id: int,
                                     _: AccountTeacher = Depends(get_current_account_teacher)):
    lesson = await LessonService.get_lesson_detail_for_edit(lesson_id)
    return LessonDetailForEditResponseCreator.get_from_lesson(lesson)


@lessons_router.get('/simple', response_model=List[LessonOnlyNameResponse])
async def get_lessons_names(course_id: int = Depends(get_course_id),
                            subject_id: int = Depends(get_subject_id),
                            pagination_params: PaginationParams = Depends()):
    lessons: List[Lesson] = await LessonService.get_lessons_names(course_id=course_id, subject_id=subject_id,
                                                                  limit=pagination_params.limit,
                                                                  skip=pagination_params.skip)
    return LessonOnlyNameResponseCreator.get_many_from_lessons(lessons)


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


@lessons_router.post('/', response_model=JustIdResponse)
async def lesson_create(account_teacher_request: AccountTeacher = Depends(get_current_account_teacher)):
    lesson: Lesson = await LessonService.create_empty_lesson(account_teacher_id=account_teacher_request.id)
    return JustIdResponseCreator.get_from_id(lesson.id)


@lessons_router.patch('/{lesson_id}', response_model=LessonDetailForEditResponse)
async def lesson_update(lesson_id: int,
                        lesson_request: LessonUpdateRequest,
                        account_teacher: AccountTeacher = Depends(get_current_account_teacher)):
    lesson = await LessonService.update_lesson(lesson_id, lesson_request, account_teacher.id)
    return LessonDetailForEditResponseCreator.get_from_lesson(lesson)


@lessons_router.patch('/{lesson_id}/status', response_model=bool)
async def update_status(lesson_id: int,
                        status_request: LessonStatusUpdateRequest,
                        account_teacher: AccountTeacher = Depends(get_current_account_teacher)):
    await LessonService.update_lesson_status(lesson_id, status_request.status, account_teacher.id)
    return True
