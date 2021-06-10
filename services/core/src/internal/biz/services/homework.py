from typing import Optional

from src.internal.biz.dao.homework.homework import HomeworkDao
from src.internal.biz.entities.biz.homework.homework import Homework
from src.internal.servers.http.exceptions.homework import HomeworkExceptionEnum


class HomeworkService:
    @staticmethod
    async def get_homework_detail_for_student(homework_id: int, account_student_id: Optional[int]) -> Homework:
        homework = await HomeworkDao().get_detail_for_student(homework_id, account_student_id)
        if not homework:
            raise HomeworkExceptionEnum.HOMEWORK_NOT_FOUND

        return homework
