from typing import Optional, List

from src.internal.biz.dao.subject import SubjectDao
from src.internal.biz.entities.biz.subject import Subject
from src.internal.biz.entities.biz.subject_course import SubjectCourse


class SubjectsService:
    @staticmethod
    async def get_all(limit: int, skip: int, course_id: Optional[int] = None):
        return await SubjectDao().get_all_subjects(limit=limit, offset=skip, course_id=course_id)

    @staticmethod
    async def get_lead_for_teacher(limit: int, skip: int, account_teacher_id: int, lesson_search: Optional[str]
                                   ) -> List[SubjectCourse]:
        return await SubjectDao().get_teacher_lead(limit, skip, account_teacher_id, lesson_search=lesson_search)

    @staticmethod
    async def get_subscribed_for_student(limit: int, skip: int, account_student_id: int) -> List[SubjectCourse]:
        return await SubjectDao().get_student_subscribed(limit, skip, account_student_id)

    @staticmethod
    async def get_teacher_subjects(limit: int, skip: int, account_teacher_id: int, course_id: int) -> List[Subject]:
        return await SubjectDao().get_teacher_subjects(limit=limit, offset=skip, account_teacher_id=account_teacher_id,
                                                       course_id=course_id)
