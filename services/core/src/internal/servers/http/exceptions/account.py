from fastapi import HTTPException


class AccountsExceptionEnum:
    WRONG_EMAIL_OR_PASSWORD = HTTPException(400, detail='Неверный email или пароль',
                                            headers={'WWW-Authenticate': 'Bearer'})
    WRONG_AUTH_TOKEN = HTTPException(status_code=401, detail='Некорректный или устаревший токен',
                                     headers={'WWW-Authenticate': 'Bearer'})
