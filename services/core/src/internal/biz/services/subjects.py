from typing import Optional

from src.internal.biz.dao.subject import SubjectDao


class SubjectsService:
    @staticmethod
    async def get_all(limit: int, skip: int, course_id: Optional[int] = None):
        return await SubjectDao().get_all_subjects(limit=limit, offset=skip, course_id=course_id)
