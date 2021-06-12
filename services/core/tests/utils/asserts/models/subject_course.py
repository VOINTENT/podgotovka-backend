from typing import Dict, Any


def assert_subject_course_simple_response(result: Dict[str, Any], subject_id: int, course_id: int, name: str):

    assert result['course_id'] == course_id
    assert result['subject_id'] == subject_id
    assert result['name'] == name
