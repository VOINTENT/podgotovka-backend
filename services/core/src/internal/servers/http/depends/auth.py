from typing import Optional

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from src.configs.internal import SECRET_KEY, ENCRYPT_ALGORITHM
from src.internal.biz.entities.biz.account.account_student import AccountStudent
from src.internal.biz.services.accounts_student import AccountsStudentService
from src.internal.servers.http.exceptions.account import AccountsExceptionEnum

oauth2_scheme_student = OAuth2PasswordBearer(tokenUrl="accounts-student/auth/base")


async def get_account_student_id_from_token(token: str = Depends(oauth2_scheme_student)) -> Optional[int]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ENCRYPT_ALGORITHM])
    except JWTError:
        return None

    try:
        account_student_id: int = int(payload.get('sub'))
    except ValueError:
        return None

    return account_student_id


async def get_optional_current_account_student(
        account_student_id: Optional[int] = Depends(get_account_student_id_from_token)) -> Optional[AccountStudent]:
    if not account_student_id:
        return None
    account_student: Optional[AccountStudent] = await AccountsStudentService.get_by_id_simple(account_student_id)
    return account_student


async def get_current_account_student(
        account_student: Optional[AccountStudent] = Depends(get_optional_current_account_student)) -> AccountStudent:
    if not account_student:
        raise AccountsExceptionEnum.WRONG_AUTH_TOKEN
    return account_student
