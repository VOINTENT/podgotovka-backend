from fastapi import HTTPException


class AccountsExceptionEnum:
    WRONG_EMAIL_OR_PASSWORD = HTTPException(400, detail='Неверный email или пароль',
                                            headers={'WWW-Authenticate': 'Bearer'})
    WRONG_AUTH_TOKEN = HTTPException(status_code=401, detail='Некорректный или устаревший токен',
                                     headers={'WWW-Authenticate': 'Bearer'})
    INVALID_VK_STATUS = HTTPException(401, "Нельзя использовать аккаунт ВК который удален, либо заблокирован")
    INVALID_VK_CODE = HTTPException(401, "Ошибка авторизации через ВК")
    ACCOUNT_ALREADY_EXISTED = HTTPException(400, "Пользователь с таким Email уже существует")
