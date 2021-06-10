from asyncpg import Record

from src.internal.biz.entities.biz.homework.homework import Homework


class HomeworkCreator:
    @staticmethod
    def get_from_record(record: Record) -> Homework:
        return Homework(
            id=record.get('homework_id'),
            homework_type=record.get('homework_type')
        )
