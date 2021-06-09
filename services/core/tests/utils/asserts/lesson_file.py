from typing import Dict, Any

from tests.utils.asserts.utils import assert_short_url_with_full_documents


def assert_file_simple_response(response: Dict[str, Any], name: str, file_link: str):
    assert response['name'] == name
    assert_short_url_with_full_documents(file_link, response['file_link'])
