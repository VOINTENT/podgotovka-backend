from src.internal.biz.entities.enum.homework_type import HomeworkTypeEnum


class HomeworkInfo:
    def __init__(self,
                 homework_id: int,
                 is_available: bool,
                 homework_type: HomeworkTypeEnum,
                 count_questions: int,
                 count_right_answers: int) -> None:
        self.count_right_answers = count_right_answers
        self.count_questions = count_questions
        self.homework_type = homework_type
        self.is_available = is_available
        self.homework_id = homework_id
