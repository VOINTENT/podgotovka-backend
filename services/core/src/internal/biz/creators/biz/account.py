from fastapi.security import OAuth2PasswordRequestForm

from src.internal.biz.creators.base import Creator
from src.internal.biz.entities.biz.account.account import Account


class AccountCreator(Creator):
    @staticmethod
    def get_from_form_data(form_data: OAuth2PasswordRequestForm) -> Account:
        return Account(
            email=form_data.username,
            password=form_data.password
        )
