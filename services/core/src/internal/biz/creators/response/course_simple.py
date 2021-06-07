from typing import List

from src.internal.biz.creators.base import Creator
from src.internal.biz.entities.biz.course import Course
from src.internal.biz.entities.response.course.simple import CourseSimpleResponse


class CourseSimpleResponseCreator(Creator):
    @classmethod
    def get_many_from_courses(cls, courses: List[Course]) -> List[CourseSimpleResponse]:
        return [cls.get_from_course(course) for course in courses]

    @staticmethod
    def get_from_course(course: Course) -> CourseSimpleResponse:
        return CourseSimpleResponse(
            id=course.id,
            name=course.name
        )
