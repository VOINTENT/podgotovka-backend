from typing import List

from src.internal.biz.creators.base import Creator
from src.internal.biz.entities.biz.document import Document
from src.internal.biz.entities.response.document.simple import DocumentSimpleResponse


class DocumentSimpleResponseCreator(Creator):
    @staticmethod
    def get_from_document(document: Document) -> DocumentSimpleResponse:
        return DocumentSimpleResponse(
            name=document.name,
            file_link=document.get_full_url()
        )

    @classmethod
    def get_many_from_documents(cls, documents: List[Document]) -> List[DocumentSimpleResponse]:
        return [cls.get_from_document(document) for document in documents]
