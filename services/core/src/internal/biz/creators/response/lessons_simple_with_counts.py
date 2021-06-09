from src.internal.biz.creators.base import Creator
from src.internal.biz.creators.response.lesson_simple import LessonSimpleResponseCreator
from src.internal.biz.entities.lessons_with_counts import LessonsWithCounts
from src.internal.biz.entities.response.lesson.simple_with_counts import LessonSimpleListWithCountsResponse


class LessonSimpleListWithCountsResponseCreator(Creator):
    @staticmethod
    def get_from_lessons_with_counts(lessons_with_counts: LessonsWithCounts) -> LessonSimpleListWithCountsResponse:
        return LessonSimpleListWithCountsResponse(
            lessons=LessonSimpleResponseCreator.get_many_from_lessons(lessons_with_counts.lessons),
            count_next=lessons_with_counts.count_next,
            count_last=lessons_with_counts.count_last
        )
