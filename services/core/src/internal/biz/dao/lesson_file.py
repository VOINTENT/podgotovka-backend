from typing import List

from src.internal.biz.entities.biz.document import Document
from src.schema.meta import lesson_file_table
from src.internal.biz.dao.base import BaseDao


class LessonFileDao(BaseDao):
    async def delete(self, lesson_id: int) -> None:
        query = lesson_file_table.delete(). \
            where(lesson_file_table.c.lesson_id == lesson_id)

        await self.execute(query)

    async def add(self, documents: List[Document], lesson_id: int) -> List[Document]:
        query = lesson_file_table.insert(). \
            values([{'lesson_id': lesson_id,
                    'file_link': doc.short_url}
                   for doc in documents]). \
            returning(lesson_file_table.c.file_link)

        await self.fetchall(query)
        return documents
