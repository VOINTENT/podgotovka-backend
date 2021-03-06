from typing import List, Optional

from fastapi import APIRouter, Depends

from src.internal.biz.creators.response.subject_simple import SubjectSimpleResponseCreator
from src.internal.biz.creators.response.subjet_course_simple import SubjectCourseSimpleResponseCreator
from src.internal.biz.entities.biz.account.account_student import AccountStudent
from src.internal.biz.entities.biz.account.account_teacher import AccountTeacher
from src.internal.biz.entities.biz.subject import Subject

from src.internal.biz.entities.response.subject.simple import SubjectSimpleResponse
from src.internal.biz.entities.response.subject.subject_course_simple import SubjectCourseSimpleResponse
from src.internal.biz.services.subjects import SubjectsService
from src.internal.servers.http.depends.auth import get_current_account_teacher, get_current_account_student
from src.internal.servers.http.depends.filters import get_course_id, get_search
from src.internal.servers.http.depends.pagination import PaginationParams

subjects_router = APIRouter(prefix='/subjects', tags=['Subjects'])


@subjects_router.get('/my/teachers', response_model=List[SubjectSimpleResponse])
async def get_my_teacher_subjects(account_teacher: AccountTeacher = Depends(get_current_account_teacher),
                                  pagination_params: PaginationParams = Depends(),
                                  course_id: int = Depends(get_course_id)):
    subjects = await SubjectsService.get_teacher_subjects(limit=pagination_params.limit, skip=pagination_params.skip,
                                                          course_id=course_id, account_teacher_id=account_teacher.id)
    return SubjectSimpleResponseCreator.get_many_from_subjects(subjects)


@subjects_router.get('/my/teachers/lead', response_model=List[SubjectCourseSimpleResponse])
async def get_my_teacher_subjects_lead(account_teacher: AccountTeacher = Depends(get_current_account_teacher),
                                       pagination_params: PaginationParams = Depends(),
                                       lesson_search: Optional[str] = Depends(get_search)):
    subject_courses = await SubjectsService.get_lead_for_teacher(
        pagination_params.limit, pagination_params.skip, account_teacher.id, lesson_search=lesson_search)

    return SubjectCourseSimpleResponseCreator.get_from_many(subject_courses)


@subjects_router.get('/my/students', response_model=List[SubjectSimpleResponse])
async def get_my_student_subjects(account_student: AccountStudent = Depends(get_current_account_student),
                                  pagination_params: PaginationParams = Depends(),
                                  course_id: int = Depends(get_course_id)):
    pass


@subjects_router.get('/my/students/subscribed', response_model=List[SubjectCourseSimpleResponse])
async def get_my_student_subjects_subscribed(account_student: AccountStudent = Depends(get_current_account_student),
                                             pagination_params: PaginationParams = Depends()):
    subject_courses = await SubjectsService.get_subscribed_for_student(pagination_params.limit,
                                                                       pagination_params.skip,
                                                                       account_student.id)
    return SubjectCourseSimpleResponseCreator.get_from_many(subject_courses)


@subjects_router.get('/', response_model=List[SubjectSimpleResponse])
async def get_all_subjects(pagination_params: PaginationParams = Depends(),
                           course_id: Optional[int] = Depends(get_course_id)):
    subjects: List[Subject] = await SubjectsService.get_all(limit=pagination_params.limit, skip=pagination_params.skip,
                                                            course_id=course_id)
    return SubjectSimpleResponseCreator.get_many_from_subjects(subjects)
