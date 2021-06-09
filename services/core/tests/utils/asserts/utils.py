import json
from typing import Optional

from src.configs.internal import FILES_LINK


def assert_short_url_with_full_documents(short_url: Optional[str], full_url: Optional[str]):
    if short_url is None and full_url is None:
        return
    assert full_url == FILES_LINK + '/documents/' + short_url


def assert_json(first_str: str, second_str: str):
    assert json.loads(first_str) == json.loads(second_str)
