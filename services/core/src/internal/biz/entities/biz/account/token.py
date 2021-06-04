from datetime import timedelta, datetime
from typing import Optional

from jose import jwt

from src.configs.internal import SECRET_KEY, ENCRYPT_ALGORITHM


class Token:

    token_type = 'bearer'

    def __init__(self, account_id: int, expires_delta: timedelta = timedelta(weeks=1)) -> None:
        self.expires_delta = expires_delta
        self.account_id = account_id
        self.auth_token: Optional[str]

    def create_auth_token(self) -> None:
        self.auth_token = jwt.encode({
            'sub': str(self.account_id),
            'exp': datetime.now() + self.expires_delta
        }, SECRET_KEY, algorithm=ENCRYPT_ALGORITHM)
