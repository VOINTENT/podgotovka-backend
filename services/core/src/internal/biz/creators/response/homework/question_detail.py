from typing import List

from src.internal.biz.creators.base import Creator
from src.internal.biz.creators.response.homework.answer_variant_detail import QuestionAnswerVariantResponseCreator
from src.internal.biz.creators.response.homework.prompt_detail import QuestionPromptResponseCreator
from src.internal.biz.entities.biz.homework.test_question import TestQuestion
from src.internal.biz.entities.response.test_question.detail import TestQuestionDetailResponse


class TestQuestionResponseCreator(Creator):
    @classmethod
    def get_from_one(cls, test_question: TestQuestion) -> TestQuestionDetailResponse:
        answer_variants = QuestionAnswerVariantResponseCreator().get_from_many(test_question.answer_variants)
        prompts = QuestionPromptResponseCreator().get_from_many(test_question.prompts)
        return TestQuestionDetailResponse(
            question_text=test_question.text,
            answer_type=test_question.answer_type,
            answer_variants=answer_variants,
            total_count_attempts=test_question.count_attempts,
            prompts=prompts
        )

    @classmethod
    def get_from_many(cls, test_questions: List[TestQuestion]) -> List[TestQuestionDetailResponse]:
        return [cls.get_from_one(test_question) for test_question in test_questions]
