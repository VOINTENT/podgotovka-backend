from typing import Dict, Any


def assert_subject_simple_response(result: Dict[str, Any], id: int, name: str):
    assert result['id'] == id
    assert result['name'] == name


def assert_subject_course_simple_response(result: Dict[str, Any], name: str, subject_id: int, course_id: int):
    assert result['name'] == name
    assert result['subject_id'] == subject_id
    assert result['course_id'] == course_id
