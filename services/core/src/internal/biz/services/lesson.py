import datetime
from typing import List, Optional

from src.internal.biz.creators.biz.lesson_with_counts import LessonWithCountsCreator
from src.internal.biz.dao.lesson import LessonDao
from src.internal.biz.entities.biz.lesson import Lesson
from src.internal.servers.http.exceptions.lesson import LessonExceptionEnum
from src.internal.biz.entities.enum.order import OrderEnum
from src.internal.biz.entities.lessons_with_counts import LessonsWithCounts
from src.internal.servers.http.exceptions.lessons import LessonsExceptionEnum


class LessonService:
    @staticmethod
    async def create_empty_lesson(account_teacher_id: int) -> Lesson:
        return await LessonDao().add(account_teacher_id)

    @staticmethod
    def _transfer_none_fields(past_state: Lesson, future_state: Lesson) -> Lesson:
        for attr, value in vars(future_state).items():
            if value is None:
                past_value = getattr(past_state, attr)
                setattr(future_state, attr, past_value)
        return future_state

    @staticmethod
    async def update_lesson(lesson: Lesson) -> Lesson:
        lesson_old_state = await LessonDao().get(lesson.id, lesson.account_teacher_id)
        if not lesson_old_state:
            raise LessonExceptionEnum.LESSON_DOESNT_EXIST

        lesson = LessonService._transfer_none_fields(lesson_old_state, lesson)

        async with LessonDao().connection_transaction() as conn:
            # TODO нужно возвращать актульное состояние из БД (сейчас возвращается то, что было отправлено)
            return await LessonDao(conn).update(lesson)

    @staticmethod
    async def get_published_lessons_with_counts(
            limit: int, skip: int, date_start: datetime.datetime, order: OrderEnum, course_id: int, subject_id: int,
            auth_account_student_id: Optional[int] = None) -> LessonsWithCounts:
        lessons: List[Lesson] = await LessonDao().get_published_lessons(
            limit=limit, offset=skip, date_start=date_start, order=order, course_id=course_id, subject_id=subject_id,
            account_student_id=auth_account_student_id
        )

        if lessons:
            count_last = await LessonDao().get_count_last(lessons[0].created_at)
            count_next = await LessonDao().get_count_next(lessons[-1].created_at)
        else:
            count_last = 0
            count_next = 0

        return LessonWithCountsCreator.get_from_args(lessons=lessons, count_last=count_last, count_next=count_next)

    @staticmethod
    async def get_lesson_detail_for_student(lesson_id: int, auth_account_student_id: int) -> Lesson:
        lesson = await LessonDao().get_detail_with_files_with_homework_info(lesson_id=lesson_id,
                                                                            account_student_id=auth_account_student_id)

        if not lesson:
            raise LessonsExceptionEnum.LESSON_NOT_FOUND
        return lesson
