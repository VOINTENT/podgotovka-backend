from typing import List

from asyncpg import Record

from src.internal.biz.creators.biz.base import CreatorBiz
from src.internal.biz.entities.biz.document import Document
from src.internal.biz.entities.request.document.add import DocumentAddRequest


class DocumentCreator(CreatorBiz):
    @staticmethod
    def get_from_record(record: Record) -> Document:
        # TODO нужно имя файла!!!
        return Document("", record.get('lesson_file_link'), "", "")

    @classmethod
    def get_many_from_document_add_request(cls, documents: List[DocumentAddRequest]) -> List[Document]:
        return [cls.get_from_document_add_request(document) for document in documents]

    @staticmethod
    def get_from_document_add_request(document: DocumentAddRequest) -> Document:
        return Document(
            name=document.name,
            optional_url=document.file_link
        )
