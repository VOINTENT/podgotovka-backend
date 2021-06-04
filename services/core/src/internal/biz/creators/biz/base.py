from abc import abstractmethod
from typing import List

from asyncpg import Record

from src.internal.biz.creators.base import Creator


class CreatorBiz(Creator):
    @abstractmethod
    def get_from_record(self, record: Record):
        pass

    def get_from_record_many(self, records: List[Record]):
        return [self.get_from_record(record) for record in records]
