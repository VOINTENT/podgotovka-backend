from asyncpg import Record

from src.internal.biz.creators.biz.base import CreatorBiz
from src.internal.biz.entities.biz.document import Document


class DocumentCreator(CreatorBiz):
    @staticmethod
    def get_from_record(record: Record) -> Document:
        # TODO нужно имя файла!!!
        return Document("", record.get('lesson_file_link'), "", "")

    @staticmethod
    def get_from_requests(url_link: str) -> Document:
        doc = Document(optional_url=url_link)
        doc.create_short_link_from_optional()
        return doc
