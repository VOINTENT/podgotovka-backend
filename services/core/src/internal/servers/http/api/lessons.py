from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends

from src.internal.biz.entities.response.lesson.detail import LessonDetailResponse
from src.internal.biz.entities.response.lesson.simple import LessonSimpleResponse

lessons_router = APIRouter(prefix='/lessons', tags=['Lessons'])


@lessons_router.get('/', response_model=List[LessonSimpleResponse])
async def get_lessons(date_start: datetime = Depends(get_date_start),
                      pagination_params: PaginationParams = Depends(get_pagination_params),
                      order: OrderEnum = Depends(get_order),
                      course_id: int = Depends(get_course_id),
                      subject_id: int = Depends(get_subject_id)):
    pass


@lessons_router.get('/{lesson_id}', response_model=LessonDetailResponse)
async def get_lesson_detail(lesson_id: int):
    pass
