from typing import Dict, Any


def assert_homework_info_response(response: Dict[str, Any], id: int, is_available: bool, type: str,
                                  count_questions: int, count_right_answers: int):
    assert response['id'] == id
    assert response['is_available'] is is_available
    assert response['type'] == type
    assert response['count_questions'] == count_questions
    assert response['count_right_answers'] == count_right_answers
