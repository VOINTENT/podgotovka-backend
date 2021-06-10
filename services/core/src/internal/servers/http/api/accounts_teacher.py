from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.internal.biz.creators.biz.account import AccountCreator
from src.internal.biz.creators.biz.token import Token
from src.internal.biz.creators.response.token_response import TokenResponseCreator
from src.internal.biz.entities.biz.account.account import Account
from src.internal.biz.entities.response.account.token import TokenResponse
from src.internal.biz.services.accounts_teacher import AccountsTeacherService

accounts_teacher_router = APIRouter(prefix='/accounts-teacher', tags=['Accounts Teacher'])


@accounts_teacher_router.post('/auth/base', response_model=TokenResponse)
async def auth_base(form_data: OAuth2PasswordRequestForm = Depends()):
    new_account: Account = AccountCreator.get_from_form_data(form_data)
    token: Token = await AccountsTeacherService.auth_account_base(new_account)
    return TokenResponseCreator.get_from_token(token)
