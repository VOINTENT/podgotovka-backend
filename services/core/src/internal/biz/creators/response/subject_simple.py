from typing import List

from src.internal.biz.creators.base import Creator
from src.internal.biz.entities.biz.subject import Subject
from src.internal.biz.entities.response.subject.simple import SubjectSimpleResponse


class SubjectSimpleResponseCreator(Creator):
    @classmethod
    def get_many_from_subjects(cls, subjects: List[Subject]) -> List[SubjectSimpleResponse]:
        return [cls.get_from_subject(subject) for subject in subjects]

    @staticmethod
    def get_from_subject(subject: Subject) -> SubjectSimpleResponse:
        return SubjectSimpleResponse(
            id=subject.id,
            name=subject.name
        )
