from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.internal.biz.creators.biz.account import AccountCreator
from src.internal.biz.creators.biz.token import Token
from src.internal.biz.creators.response.token_response import TokenResponseCreator
from src.internal.biz.entities.biz.account.account import Account
from src.internal.biz.entities.response.account.token import TokenResponse
from src.internal.biz.services.account import AccountTeacherService

accounts_router = APIRouter(prefix='/accounts', tags=['Teacher Accounts'])


@accounts_router.post('/auth/base', response_model=TokenResponse)
async def auth_base(form_data: OAuth2PasswordRequestForm = Depends()):
    new_account: Account = AccountCreator().get_from_form_data(form_data)
    token: Token = await AccountTeacherService.auth_account_base(new_account)
    return TokenResponseCreator().get_from_token(token)
