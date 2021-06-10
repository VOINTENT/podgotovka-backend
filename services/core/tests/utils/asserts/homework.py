from typing import Dict, Any, List, Optional

from tests.utils.asserts.utils import assert_json


def assert_homework_info_response(response: Dict[str, Any], id: int, is_available: bool, type: str,
                                  count_questions: int, count_right_answers: int):
    assert response['id'] == id
    assert response['is_available'] is is_available
    assert response['type'] == type
    assert response['count_questions'] == count_questions
    assert response['count_right_answers'] == count_right_answers


def assert_homework_detail_with_results_response(
        response: Dict[str, Any], id: int, homework_type: str, homework_without_answer: Optional[Dict[str, Any]],
        homework_test: Optional[Dict[str, Any]]):
    assert response['id'] == id
    assert response['type'] == homework_type

    if homework_without_answer is None:
        assert response['homework_without_answer'] is None
    else:
        assert_homework_without_answer_detail_response(
            response['homework_without_answer'], question=homework_without_answer['question'])

    if homework_test is None:
        assert response['homework_test'] is None
    assert_homework_test_detail_with_results_response(response['homework_test'],
                                                      test_questions=homework_test['test_questions'])


def assert_homework_without_answer_detail_response(response: Dict[str, Any], question: str):
    assert_json(response['question'], question)


def assert_homework_test_detail_with_results_response(response: Dict[str, Any], test_questions: List[Dict[str, Any]]):
    for test_question_response, test_question in zip(response['test_questions'], test_questions):
        assert_test_question_detail_with_result_response(
            test_question_response, id=test_question['id'], name=test_question['question_name'], question_text=test_question['question_text'],
            answer_type=test_question['answer_type'], answer_variants=test_question['answer_variants'],
            total_count_attempts=test_question['total_count_attempts'],
            available_count_attempts=test_question['available_count_attempts'],
            used_prompts=test_question['used_prompts'], unused_prompts=test_question['unused_prompts'])


def assert_test_question_detail_with_result_response(
        response: Dict[str, Any], id: int, name: str, question_text: str, answer_type: str, answer_variants: Optional[List[Dict[str, Any]]],
        total_count_attempts: int, available_count_attempts: int, used_prompts: List[Dict[str, Any]],
        unused_prompts: List[Dict[str, Any]]):
    assert response['id'] == id
    assert response['question_name'] == name
    assert_json(response['question_text'], question_text)
    assert response['answer_type'] == answer_type
    assert response['total_count_attempts'] == total_count_attempts
    assert response['available_count_attempts'] == available_count_attempts

    if answer_variants is None:
        assert response['answer_variants'] is None
    else:
        for answer_variant_response, answer_variant in zip(response['answer_variants'], answer_variants):
            assert_answer_variant_simple_response(answer_variant_response, id=answer_variant['id'],
                                                  name=answer_variant['name'])

    for used_prompt_response, used_prompt in zip(response['used_prompts'], used_prompts):
        assert_prompt_simple_response(used_prompt_response, text=used_prompt['text'])

    for unused_prompt_response, unused_prompt in zip(response['unused_prompts'], unused_prompts):
        assert_prompt_simple_response(unused_prompt_response, text=unused_prompt['text'])


def assert_prompt_simple_response(response: Dict[str, Any], text: str):
    assert_json(response['text'], text)


def assert_answer_variant_simple_response(response: Dict[str, Any], id: int, name: str):
    assert response['id'] == id
    assert response['name'] == name
