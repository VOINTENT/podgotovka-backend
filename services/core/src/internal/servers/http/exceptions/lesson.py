from fastapi import HTTPException


class LessonExceptionEnum:
    LESSON_DOESNT_EXIST = HTTPException(400, "Такого урока не существует")
    LESSON_INCORRECT_HOMEWORK_TYPE = HTTPException(400, "Неизвестный формат домашнего задания")
    LESSON_HOMEWORK_COUNT_ANSWER = HTTPException(400, "Для данного формата кол-во ответов должно быть больше одного")
    LESSON_QUESTION_ONE_MANY_TRUE_ANSWER = HTTPException(400,
                                                         "У вопроса c единичным выбором может быть только один правильный ответ")
