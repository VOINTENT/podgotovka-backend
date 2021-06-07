from typing import Dict, Any


def assert_simple_course_response(result: Dict[str, Any], id: int, name: str):
    assert result['id'] == id
    assert result['name'] == name
