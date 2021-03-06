from src.internal.biz.creators.base import Creator
from src.internal.biz.entities.biz.account.account import Account
from src.internal.biz.entities.biz.account.token import Token


class TokenCreator(Creator):
    @staticmethod
    def get_from_account(account: Account) -> Token:
        return Token(account_id=account.id)
