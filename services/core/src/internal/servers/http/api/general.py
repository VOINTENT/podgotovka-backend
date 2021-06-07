from fastapi import APIRouter

from src.extra.entities.response.exceptions.base import ExceptionResponse
from src.internal.servers.http.api.accounts_student import accounts_student_router
from src.internal.servers.http.api.accounts_teacher import teacher_accounts_router
from src.internal.servers.http.api.courses import courses_router
from src.internal.servers.http.api.homeworks import homeworks_router
from src.internal.servers.http.api.lessons import lessons_router
from src.internal.servers.http.api.subjects import subjects_router

general_router = APIRouter(prefix='/core/v1', responses={400: {'model': ExceptionResponse},
                                                         500: {'model': ExceptionResponse}})

general_router.include_router(teacher_accounts_router)
general_router.include_router(accounts_student_router)
general_router.include_router(homeworks_router)
general_router.include_router(lessons_router)
general_router.include_router(subjects_router)
general_router.include_router(courses_router)
