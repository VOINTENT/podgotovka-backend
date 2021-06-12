from fastapi import HTTPException


class LessonExceptionEnum:
    LESSON_DOESNT_EXIST = HTTPException(404, "Такого урока не существует")
    LESSON_INCORRECT_HOMEWORK_TYPE = HTTPException(400, "Неизвестный формат домашнего задания")
    LESSON_HOMEWORK_COUNT_ANSWER = HTTPException(400, "Для данного формата кол-во ответов должно быть больше одного")
    LESSON_FORBIDDEN = HTTPException(403, "Запрещено для данного урока")
    LESSON_QUESTION_ONE_MANY_TRUE_ANSWER = HTTPException(
        400, "У вопроса c единичным выбором может быть только один правильный ответ")
    LESSON_NOT_SUBJECT = HTTPException(400, 'Не указан предмет')
    LESSON_NOT_COURSE = HTTPException(400, 'Не указан класс')
    LESSON_NOT_NAME = HTTPException(400, 'Не указано название урока')
    LESSON_NOT_YOUTUBE_LINK = HTTPException(400, 'Не указана ссылка на видео')
    LESSON_NOT_DATETIME_START = HTTPException(400, 'Не указаны дата и время начала')
