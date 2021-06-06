from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.internal.biz.entities.request.account.student.add import AccountStudentAddRequest
from src.internal.biz.entities.request.auth.vk_code import VkCodeRequest
from src.internal.biz.entities.response.account.token import TokenResponse

accounts_student_router = APIRouter(prefix='/accounts-student', tags=['Student Accounts'])


@accounts_student_router.post('/register', response_model=TokenResponse)
async def register_student(student_account_request: AccountStudentAddRequest):
    pass


@accounts_student_router.get('/auth/base', response_model=TokenResponse)
async def auth_base_student(form_data: OAuth2PasswordRequestForm = Depends()):
    pass


@accounts_student_router.get('/auth/vk', response_model=TokenResponse)
async def auth_or_register_student_by_vk(vk_code_request: VkCodeRequest):
    pass
