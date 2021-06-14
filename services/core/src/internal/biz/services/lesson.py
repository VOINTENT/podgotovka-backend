import datetime
from typing import List, Optional, Tuple

from src.internal.biz.creators.biz.lesson import LessonCreator
from src.internal.biz.creators.biz.lesson_with_counts import LessonWithCountsCreator
from src.internal.biz.dao.lesson import LessonDao
from src.internal.biz.entities.biz.lesson import Lesson
from src.internal.biz.entities.enum.lesson_status import LessonStatusEnum
from src.internal.biz.entities.request.lesson.update import LessonUpdateRequest
from src.internal.servers.http.exceptions.lesson import LessonExceptionEnum
from src.internal.biz.entities.enum.order import OrderEnum
from src.internal.biz.entities.lessons_with_counts import LessonsWithCounts
from src.internal.servers.http.exceptions.lessons import LessonsExceptionEnum


class LessonService:
    @staticmethod
    async def create_empty_lesson(account_teacher_id: int) -> Lesson:
        lesson = LessonCreator.get_empty(account_teacher_id=account_teacher_id)
        return await LessonDao().add(lesson)

    @staticmethod
    async def get_lesson_detail_for_edit(lesson_id: int) -> Lesson:
        lesson_exist = await LessonDao().exist(lesson_id)
        if not lesson_exist:
            raise LessonExceptionEnum.LESSON_DOESNT_EXIST

        lesson = await LessonDao().get_with_files(lesson_id)
        return lesson

    @staticmethod
    async def update_lesson(lesson_id: int, lesson_request: LessonUpdateRequest,
                            auth_account_teacher_id: int) -> Lesson:
        existed_lesson = await LessonDao().get(lesson_id)
        if not existed_lesson:
            raise LessonExceptionEnum.LESSON_DOESNT_EXIST

        if existed_lesson.account_teacher_id != auth_account_teacher_id:
            raise LessonExceptionEnum.LESSON_FORBIDDEN

        new_lesson = LessonCreator.get_from_existed_and_updated(existed_lesson, lesson_request)
        await LessonDao().update(lesson_id, new_lesson)
        return await LessonDao().get_with_files(lesson_id)

    @classmethod
    async def get_published_lessons_with_counts(
            cls, limit: int, skip: int, date_start: datetime.datetime, order: OrderEnum, course_id: int,
            subject_id: int, auth_account_student_id: Optional[int] = None,
            date_finish: Optional[datetime.datetime] = None
    ) -> LessonsWithCounts:
        lessons: List[Lesson] = await LessonDao().get_published_lessons(
            limit=limit, offset=skip, date_start=date_start, order=order, course_id=course_id, subject_id=subject_id,
            account_student_id=auth_account_student_id, date_finish=date_finish
        )

        count_last, count_next = await cls._get_counts_other_lessons(
            lessons, course_id=course_id, subject_id=subject_id, account_teacher_id=None)
        return LessonWithCountsCreator.get_from_args(lessons=lessons, count_last=count_last, count_next=count_next)

    @staticmethod
    async def get_lesson_detail_for_student(lesson_id: int, auth_account_student_id: int) -> Lesson:
        lesson = await LessonDao().get_detail_with_files_with_homework_info(lesson_id=lesson_id,
                                                                            account_student_id=auth_account_student_id)

        if not lesson:
            raise LessonsExceptionEnum.LESSON_NOT_FOUND
        return lesson

    @classmethod
    async def get_lessons_for_teacher(
            cls, account_teacher_id: int, limit: int, skip: int, date_start: datetime.datetime,
            date_finish: datetime.datetime, order: OrderEnum, course_id: Optional[int], subject_id: Optional[int]
    ) -> LessonsWithCounts:
        lessons: List[Lesson] = await LessonDao().get_published_lessons_by_teacher(
            account_teacher_id=account_teacher_id, limit=limit, offset=skip, date_start=date_start, order=order,
            course_id=course_id, subject_id=subject_id, date_finish=date_finish
        )

        count_last, count_next = await cls._get_counts_other_lessons(
            lessons, course_id=course_id, subject_id=subject_id, account_teacher_id=account_teacher_id)
        return LessonWithCountsCreator.get_from_args(lessons=lessons, count_last=count_last, count_next=count_next)

    @staticmethod
    async def get_lessons_names(course_id: int, subject_id: int, limit: int, skip: int, lesson_search: Optional[str]) -> List[Lesson]:
        lessons: List[Lesson] = await LessonDao().get_names(
            course_id=course_id, subject_id=subject_id, limit=limit, offset=skip, lesson_search=lesson_search)
        return lessons

    @staticmethod
    async def _get_counts_other_lessons(lessons: List[Lesson], course_id: Optional[int], subject_id: Optional[int],
                                        account_teacher_id: Optional[int]) -> Tuple[int, int]:
        if not lessons:
            return 0, 0

        min_created_at = min(lessons[0].created_at, lessons[-1].created_at)
        max_created_at = max(lessons[0].created_at, lessons[-1].created_at)
        count_last = await LessonDao().get_count_last(min_created_at, course_id=course_id, subject_id=subject_id,
                                                      account_teacher_id=account_teacher_id)
        count_next = await LessonDao().get_count_next(max_created_at, course_id=course_id, subject_id=subject_id,
                                                      account_teacher_id=account_teacher_id)
        return count_last, count_next

    @staticmethod
    async def update_lesson_status(lesson_id: int, lesson_status: LessonStatusEnum,
                                   auth_account_teacher_id: int) -> None:
        owner_account_teacher_id = await LessonDao().get_owner_account_teacher_id(lesson_id)
        if not owner_account_teacher_id:
            raise LessonExceptionEnum.LESSON_DOESNT_EXIST

        if owner_account_teacher_id != auth_account_teacher_id:
            raise LessonExceptionEnum.LESSON_DOESNT_EXIST

        if lesson_status == LessonStatusEnum.published:
            lesson: Lesson = await LessonDao().get_with_files(lesson_id)
            lesson.validate()

        await LessonDao().update_status(lesson_id, lesson_status)
