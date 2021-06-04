from fastapi import HTTPException


class AccountsExceptionEnum:
    WRONG_EMAIL_OR_PASSWORD = HTTPException(400, detail='Неверный email или пароль',
                                            headers={'WWW-Authenticate': 'Bearer'})
