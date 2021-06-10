from typing import Optional

from src.internal.biz.dao.homework import HomeworkDao
from src.internal.biz.entities.biz.homework.homework import Homework


class HomeworkService:
    @staticmethod
    async def get_homework_detail_for_student(homework_id: int, account_student_id: Optional[int]) -> Homework:
        return await HomeworkDao().get_detail_for_student(homework_id, account_student_id)
