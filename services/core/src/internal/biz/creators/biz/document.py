from typing import List

from asyncpg import Record

from src.internal.biz.creators.biz.base import CreatorBiz
from src.internal.biz.entities.biz.document import Document


class DocumentCreator(CreatorBiz):
    @staticmethod
    def get_from_record(record: Record):
        return Document(
            name=record.get('lesson_document_name'),
            short_url=record.get('lesson_document_file_link')
        )

    @classmethod
    def get_many_from_record(cls, records: List[Record]) -> List[Document]:
        return [cls.get_from_record(record) for record in records]
