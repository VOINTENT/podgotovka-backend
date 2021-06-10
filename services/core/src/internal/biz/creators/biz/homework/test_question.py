from asyncpg import Record

from src.internal.biz.creators.biz.base import CreatorBiz
from src.internal.biz.creators.biz.homework.question_answer_variant import AnswerVariantCreator
from src.internal.biz.creators.biz.homework.question_prompt import PromptCreator
from src.internal.biz.entities.biz.homework.test_question import TestQuestion
from src.internal.biz.entities.enum.answer_type import AnswerTypeEnum
from src.internal.biz.entities.request.homeworks.test.question.add import TestQuestionRequest
from src.internal.servers.http.exceptions.lesson import LessonExceptionEnum


class HomeworkTestQuestionCreator(CreatorBiz):
    def get_from_request(self, test_question_request: TestQuestionRequest) -> TestQuestion:
        prompts = [PromptCreator().get_from_request(prompt)
                   for prompt in test_question_request.prompts]
        answer_type = test_question_request.answer_type
        answers = [AnswerVariantCreator().get_from_request(answer)
                   for answer in test_question_request.answer_variants]

        if answer_type == AnswerTypeEnum.one or answer_type == AnswerTypeEnum.many:
            if len(answers) < 2:
                raise LessonExceptionEnum.LESSON_HOMEWORK_COUNT_ANSWER

        is_right_count = [answer.is_right for answer in answers if answer.is_right is True]

        if answer_type == AnswerTypeEnum.one and len(is_right_count) > 1:
            raise LessonExceptionEnum.LESSON_QUESTION_ONE_MANY_TRUE_ANSWER

        return TestQuestion(
            text=test_question_request.question_text,
            count_attempts=test_question_request.total_count_attempts,
            prompts=prompts,
            answer_type=test_question_request.answer_type,
            answer_variants=answers,
        )

    def get_from_record(self, record: Record):
        pass
