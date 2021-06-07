from fastapi import APIRouter, Depends

from src.internal.biz.entities.biz.account.account_teacher import AccountTeacher
from src.internal.biz.entities.response.course.simple import CourseSimpleResponse
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
    pass


@courses_router.get('/my/students', response_model=CourseSimpleResponse)
async def get_my_students_courses(
        account_teacher: AccountTeacher = Depends(get_current_account_teacher),
        pagination_params: PaginationParams = Depends(),
        subject_id: int = Depends(get_subject_id)
):
    pass
