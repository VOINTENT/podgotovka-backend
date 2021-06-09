from fastapi import HTTPException


class LessonsExceptionEnum:
    LESSON_NOT_FOUND = HTTPException(404, detail='Данный урок не найден')
