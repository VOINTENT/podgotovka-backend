from src.internal.biz.creators.base import Creator
from src.internal.biz.entities.biz.homework.info import HomeworkInfo
from src.internal.biz.entities.response.homework.info import HomeworkInfoResponse


class HomeworkInfoResponseCreator(Creator):
    @staticmethod
    def get_from_homework_info(homework_info: HomeworkInfo) -> HomeworkInfoResponse:
        return HomeworkInfoResponse(
            id=homework_info.homework_id,
            is_available=homework_info.is_available,
            type=homework_info.homework_type,
            count_questions=homework_info.count_questions,
            count_right_answers=homework_info.count_right_answers
        )
