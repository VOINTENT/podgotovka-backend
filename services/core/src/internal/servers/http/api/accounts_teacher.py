from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.internal.biz.creators.biz.account import AccountCreator
from src.internal.biz.creators.biz.token import Token
from src.internal.biz.creators.response.account.teacher_detail import AccountTeacherDetailResponseCreator
from src.internal.biz.creators.response.token_response import TokenResponseCreator
from src.internal.biz.entities.biz.account.account import Account
from src.internal.biz.entities.biz.account.account_teacher import AccountTeacher
from src.internal.biz.entities.response.account.teacher_detail import AccountTeacherDetailResponse
from src.internal.biz.entities.response.account.token import TokenResponse
from src.internal.biz.services.accounts_teacher import AccountsTeacherService
from src.internal.servers.http.depends.auth import get_current_account_teacher

accounts_teacher_router = APIRouter(prefix='/accounts-teacher', tags=['Accounts Teacher'])


@accounts_teacher_router.post('/auth/base', response_model=TokenResponse)
async def auth_base(form_data: OAuth2PasswordRequestForm = Depends()):
    new_account: Account = AccountCreator.get_from_form_data(form_data)
    token: Token = await AccountsTeacherService.auth_account_base(new_account)
    return TokenResponseCreator.get_from_token(token)


@accounts_teacher_router.get('/me', response_model=AccountTeacherDetailResponse)
async def get_detail_info_about_student(account_teacher: AccountTeacher = Depends(get_current_account_teacher)):
    teacher = await AccountsTeacherService.get_by_id_detail(account_teacher.id)
    return AccountTeacherDetailResponseCreator.get_from_one(teacher)
