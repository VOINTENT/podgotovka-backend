from fastapi import HTTPException


class ServerExceptionsEnum:
    UNKNOWN_SERVER_ERROR = HTTPException(status_code=500, detail='Неизвестная ошибка сервера')
