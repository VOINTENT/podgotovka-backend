from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.internal.biz.creators.biz.account import AccountCreator
from src.internal.biz.creators.biz.account_student import AccountStudentCreator
from src.internal.biz.creators.response.token_response import TokenResponseCreator
from src.internal.biz.entities.request.account.student.add import AccountStudentAddRequest
from src.internal.biz.entities.request.auth.vk_code import VkCodeRequest
from src.internal.biz.entities.response.account.token import TokenResponse
from src.internal.biz.services.accounts_student import AccountsStudentService

accounts_student_router = APIRouter(prefix='/accounts-student', tags=['Student Accounts'])


@accounts_student_router.post('/register', response_model=TokenResponse)
async def register_student(account_student_request: AccountStudentAddRequest):
    student = AccountStudentCreator.get_from_request(account_student_request)
    student.create_hash_password()
    token = await AccountsStudentService.register_account(student)
    return TokenResponseCreator.get_from_token(token)


@accounts_student_router.post('/auth/base', response_model=TokenResponse)
async def auth_base_student(form_data: OAuth2PasswordRequestForm = Depends()):
    new_account = AccountCreator().get_from_form_data(form_data)
    token = await AccountsStudentService.auth_account_base(new_account)
    return TokenResponseCreator().get_from_token(token)


@accounts_student_router.post('/auth/vk', response_model=TokenResponse)
async def auth_or_register_student_by_vk(vk_code_request: VkCodeRequest):
    token = await AccountsStudentService.auth_or_register_by_vk(vk_code_request.code)
    return TokenResponseCreator().get_from_token(token)
