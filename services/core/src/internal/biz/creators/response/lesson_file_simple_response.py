from typing import List

from src.internal.biz.creators.base import Creator
from src.internal.biz.entities.biz.document import Document
from src.internal.biz.entities.response.lesson.lesson_file import LessonFileSimpleResponse


class LessonFileSimpleResponseCreator(Creator):
    @classmethod
    def get_many_from_documents(cls, documents: List[Document]) -> List[LessonFileSimpleResponse]:
        return [cls.get_from_document(document) for document in documents]

    @staticmethod
    def get_from_document(document: Document) -> LessonFileSimpleResponse:
        return LessonFileSimpleResponse(
            name=document.name,
            file_link=document.get_full_url()
        )
