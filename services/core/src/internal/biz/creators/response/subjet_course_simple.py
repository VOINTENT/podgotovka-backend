from typing import List

from src.internal.biz.creators.base import Creator
from src.internal.biz.entities.biz.subject_course import SubjectCourse
from src.internal.biz.entities.response.subject.subject_course_simple import SubjectCourseSimpleResponse


class SubjectCourseSimpleResponseCreator(Creator):
    @classmethod
    def get_from_one(cls, subject_course: SubjectCourse) -> SubjectCourseSimpleResponse:
        return SubjectCourseSimpleResponse(
            name=subject_course.name,
            subject_id=subject_course.subject_id,
            course_id=subject_course.course_id,
        )

    @classmethod
    def get_from_many(cls, subjects_courses: List[SubjectCourse]):
        return [cls.get_from_one(subject_course) for subject_course in subjects_courses]
