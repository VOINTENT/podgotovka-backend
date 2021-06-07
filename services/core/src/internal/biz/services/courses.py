from typing import List

from src.internal.biz.dao.course import CourseDao
from src.internal.biz.entities.biz.course import Course


class CoursesService:
    @staticmethod
    async def get_all(limit: int, skip: int, subject_id: int) -> List[Course]:
        return await CourseDao().get_all_courses(limit=limit, offset=skip, subject_id=subject_id)
