from starlette.testclient import TestClient

from tests.test_data import TestHomeworkData, TestQuestionData, TestAnswerVariantData, TestAnswerVariantData2, \
    TestQuestionData2, TestAnswerVariantData3, TestAnswerVariantData4
from tests.utils.asserts.models.homework import assert_homework_detail_with_results_response


def test_get_homework_detail_for_student(client: TestClient, truncate, homework):
    response = client.get(f'/core/v1/homeworks/{TestHomeworkData.id}/students')
    assert response.status_code == 200

    response_json = response.json()
    assert_homework_detail_with_results_response(
        response_json, id=TestHomeworkData.id, homework_type=TestHomeworkData.homework_type,
        homework_without_answer=None, homework_test={
            'test_questions': [
                {
                    'id': TestQuestionData.id,
                    'question_name': TestQuestionData.name,
                    'question_text': TestQuestionData.description,
                    'answer_type': TestQuestionData.answer_type,
                    'total_count_attempts': TestQuestionData.count_attempts,
                    'available_count_attempts': TestQuestionData.count_attempts,
                    'answer_variants': [
                        {
                            'id': TestAnswerVariantData.id,
                            'name': TestAnswerVariantData.name
                        },
                        {
                            'id': TestAnswerVariantData2.id,
                            'name': TestAnswerVariantData2.name
                        }
                    ],
                    'used_prompts': [],
                    'unused_prompts': []
                },
                {
                    'id': TestQuestionData2.id,
                    'question_name': TestQuestionData2.name,
                    'question_text': TestQuestionData2.description,
                    'answer_type': TestQuestionData2.answer_type,
                    'total_count_attempts': TestQuestionData2.count_attempts,
                    'available_count_attempts': TestQuestionData2.count_attempts,
                    'answer_variants': [
                        {
                            'id': TestAnswerVariantData3.id,
                            'name': TestAnswerVariantData3.name
                        },
                        {
                            'id': TestAnswerVariantData4.id,
                            'name': TestAnswerVariantData4.name
                        }
                    ],
                    'used_prompts': [],
                    'unused_prompts': []
                }
            ]
        })
