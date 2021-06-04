from abc import ABC
from typing import Optional

from src.internal.drivers.crypt_driver import CryptDriver


class Account(ABC):
    def __init__(self, id: Optional[int] = None, password: Optional[str] = None, hash_password: Optional[str] = None,
                 email: Optional[str] = None) -> None:
        self.hash_password = hash_password
        self.password = password
        self.id = id
        self.email = email

    def is_password_valid(self, password: str) -> bool:
        return CryptDriver.context.verify(password, self.hash_password)
