from typing import List

from src.internal.biz.creators.base import Creator
from src.internal.biz.creators.response.answer_variant_simple import AnswerVariantSimpleResponseCreator
from src.internal.biz.creators.response.prompt_simple import PromptSimpleResponseCreator
from src.internal.biz.entities.biz.homework.test_question import TestQuestion
from src.internal.biz.entities.response.test_question.detail_with_result import TestQuestionDetailWithResultResponse
from src.internal.biz.entities.response.test_question.result.previous import TestQuestionResultPreviousResponse


class TestQuestionDetailWithResultResponseCreator(Creator):
    @classmethod
    def get_many_from_test_questions(cls, test_questions: List[TestQuestion]) -> List[TestQuestionDetailWithResultResponse]:
        return [cls.get_from_test_question(test_question) for test_question in test_questions]

    @staticmethod
    def get_from_test_question(test_question: TestQuestion) -> TestQuestionDetailWithResultResponse:
        return TestQuestionDetailWithResultResponse(
            id=test_question.id,
            question_name=test_question.name,
            question_text=test_question.text,
            answer_type=test_question.answer_type,
            answer_variants=AnswerVariantSimpleResponseCreator.get_many_from_answer_variants(
                test_question.answer_variants),
            total_count_attempts=test_question.count_attempts,
            unused_prompts=PromptSimpleResponseCreator.get_many_from_prompts(test_question.prompts),
            available_count_attempts=test_question.count_attempts,
            result=TestQuestionResultPreviousResponse(),
            used_prompts=[]
        )
