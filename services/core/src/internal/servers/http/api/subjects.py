from typing import List, Optional

from fastapi import APIRouter, Depends

from src.internal.biz.creators.response.subject_simple import SubjectSimpleResponseCreator
from src.internal.biz.entities.biz.account.account_student import AccountStudent
from src.internal.biz.entities.biz.account.account_teacher import AccountTeacher
from src.internal.biz.entities.biz.subject import Subject
from src.internal.biz.entities.response.subject.simple import SubjectSimpleResponse
from src.internal.biz.services.subjects import SubjectsService
from src.internal.servers.http.depends.auth import get_current_account_teacher, get_current_account_student
from src.internal.servers.http.depends.filters import get_course_id
from src.internal.servers.http.depends.pagination import PaginationParams

subjects_router = APIRouter(prefix='/subjects', tags=['Subjects'])


@subjects_router.get('/my/teachers', response_model=List[SubjectSimpleResponse])
async def get_my_teacher_subjects(account_teacher: AccountTeacher = Depends(get_current_account_teacher),
                                  pagination_params: PaginationParams = Depends(),
                                  course_id: int = Depends(get_course_id)):
    pass


@subjects_router.get('/my/students', response_model=List[SubjectSimpleResponse])
async def get_my_student_subjects(account_student: AccountStudent = Depends(get_current_account_student),
                                  pagination_params: PaginationParams = Depends(),
                                  course_id: int = Depends(get_course_id)):
    pass


@subjects_router.get('/', response_model=List[SubjectSimpleResponse])
async def get_all_subjects(pagination_params: PaginationParams = Depends(),
                           course_id: Optional[int] = Depends(get_course_id)):
    subjects: List[Subject] = await SubjectsService.get_all(limit=pagination_params.limit, skip=pagination_params.skip,
                                                            course_id=course_id)
    return SubjectSimpleResponseCreator.get_many_from_subjects(subjects)
