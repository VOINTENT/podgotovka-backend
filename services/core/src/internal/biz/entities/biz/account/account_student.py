from typing import Optional

from src.internal.biz.entities.biz.account.account import Account
from src.internal.biz.entities.biz.photo import Photo


class AccountStudent(Account):
    def __init__(self,
                 id: Optional[int] = None,
                 name: Optional[str] = None,
                 last_name: Optional[str] = None,
                 middle_name: Optional[str] = None,
                 photo: Optional[Photo] = None,
                 description: Optional[str] = None,
                 email: Optional[str] = None,
                 password: Optional[str] = None,
                 hash_password: Optional[str] = None
                 ) -> None:
        super().__init__(id, password, hash_password, email)
        self.description = description
        self.photo = photo
        self.middle_name = middle_name
        self.last_name = last_name
        self.name = name
