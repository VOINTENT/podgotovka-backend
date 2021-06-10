from typing import List

from src.internal.biz.creators.base import Creator
from src.internal.biz.entities.biz.document import Document


class LessonFileSimpleResponseCreator(Creator):
    @staticmethod
    def get_from_one(doc: Document) -> str:
        return doc.short_url

    @staticmethod
    def get_from_many(docs: List[Document]) -> List[str]:
        return [doc.short_url for doc in docs]
