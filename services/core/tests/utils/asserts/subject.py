from typing import Dict, Any


def assert_subject_simple_response(result: Dict[str, Any], id: int, name: str):
    assert result['id'] == id
    assert result['name'] == name
