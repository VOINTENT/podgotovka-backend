from typing import Optional

from pydantic import Field

from src.internal.biz.entities.request.base import BaseRequestModel


class AccountStudentAddRequest(BaseRequestModel):
    email: str = Field(..., example='email@mail.ru', min_length=4, max_length=100)
    name: str = Field(..., example='Имя', max_length=100)
    last_name: Optional[str] = Field(None, example='Фамилия', max_length=100)
    middle_name: Optional[str] = Field(None, example='Отчество', max_length=100)
    description: Optional[str] = Field(None, example='Описание', max_length=5000)
    photo_link: Optional[str] = Field(None, example='short or full link', max_length=500)
    password: str = Field(..., example='qwerty123', min_length=6, max_length=100)
