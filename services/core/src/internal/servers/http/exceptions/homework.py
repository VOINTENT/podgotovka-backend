from fastapi import HTTPException


class HomeworkExceptionEnum:
    HOMEWORK_NOT_FOUND = HTTPException(404, detail='Данное домашнее задание не найдено')
