import json
import random
import uuid
from datetime import datetime
from string import digits, ascii_letters
from typing import Optional


def get_random_digits(length: Optional[int] = None) -> str:
    if not length:
        length = random.randint(3, 100)
    return ''.join(random.choice(digits) for _ in range(length))


def get_random_uuid() -> str:
    return uuid.uuid4().hex


def get_random_str(length: Optional[int] = None) -> str:
    if not length:
        length = random.randint(10, 100)
    return ''.join(random.choice(ascii_letters + digits) for _ in range(length))


def get_random_int(max_value: Optional[int] = 2_000_000_000) -> int:
    return random.randint(1, max_value)


def get_random_email(length: Optional[int] = None) -> str:
    if not length:
        length = random.randint(3, 90)
    return get_random_str(length) + '@mail.ru'


def get_random_phone() -> str:
    return '+7' + get_random_digits(10)


def get_random_datetime() -> datetime:
    return random.choice([datetime(year=year, month=1, day=1) for year in range(1970, 2021)])


def get_auth_headers(access_token: str) -> dict:
    return {
        'Authorization': f'Bearer {access_token}'
    }

def get_random_json(length: Optional[int] = None) -> str:
    if not length:
        length = random.randint(3, 10)
    return json.dumps({get_random_str(3): get_random_str(4) for _ in range(length)})
