from abc import abstractmethod
from typing import List

from asyncpg import Record

from src.internal.biz.creators.base import Creator


class CreatorBiz(Creator):
    @staticmethod
    @abstractmethod
    def get_from_record(record: Record):
        pass

    @classmethod
    def get_from_record_many(cls, records: List[Record]):
        return [cls.get_from_record(record) for record in records]
