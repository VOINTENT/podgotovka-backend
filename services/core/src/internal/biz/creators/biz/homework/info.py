from typing import Optional

from asyncpg import Record

from src.internal.biz.creators.biz.base import CreatorBiz
from src.internal.biz.entities.biz.homework.info import HomeworkInfo


class HomeworkInfoCreator(CreatorBiz):
    @staticmethod
    def get_from_record(record: Record) -> Optional[HomeworkInfo]:
        if not record.get('homework_id'):
            return None
        return HomeworkInfo(
            homework_id=record.get('homework_id'),
            is_available=record.get('homework_is_available'),
            count_questions=record.get('homework_count_questions'),
            count_right_answers=record.get('homework_count_right_answers'),
            homework_type=record.get('homework_type')
        )
