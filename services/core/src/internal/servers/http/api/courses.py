from typing import List, Optional

from fastapi import APIRouter, Depends

from src.internal.biz.creators.response.course_simple import CourseSimpleResponseCreator
from src.internal.biz.entities.biz.account.account_teacher import AccountTeacher
from src.internal.biz.entities.biz.course import Course
from src.internal.biz.entities.response.course.simple import CourseSimpleResponse
from src.internal.biz.services.courses import CoursesService
from src.internal.servers.http.depends.auth import get_current_account_teacher
from src.internal.servers.http.depends.filters import get_subject_id
from src.internal.servers.http.depends.pagination import PaginationParams

courses_router = APIRouter(prefix='/courses', tags=['Courses'])


@courses_router.get('/my/teachers', response_model=CourseSimpleResponse)
async def get_my_teacher_courses(
        account_teacher: AccountTeacher = Depends(get_current_account_teacher),
        pagination_params: PaginationParams = Depends(),
        subject_id: int = Depends(get_subject_id)
):
    courses = await CoursesService.get_teacher_courses(limit=pagination_params.limit, skip=pagination_params.skip,
                                                       subject_id=subject_id, account_teacher_id=account_teacher.id)
    return CourseSimpleResponseCreator.get_many_from_courses(courses)


@courses_router.get('/my/students', response_model=CourseSimpleResponse)
async def get_my_students_courses(
        account_teacher: AccountTeacher = Depends(get_current_account_teacher),
        pagination_params: PaginationParams = Depends(),
        subject_id: int = Depends(get_subject_id)
):
    pass


@courses_router.get('/', response_model=List[CourseSimpleResponse])
async def get_all_courses(pagination_params: PaginationParams = Depends(),
                          subject_id: Optional[int] = Depends(get_subject_id)):
    courses: List[Course] = await CoursesService.get_all(limit=pagination_params.limit, skip=pagination_params.skip,
                                                         subject_id=subject_id)
    return CourseSimpleResponseCreator.get_many_from_courses(courses)
