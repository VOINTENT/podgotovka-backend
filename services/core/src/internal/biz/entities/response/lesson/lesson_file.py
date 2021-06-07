from pydantic import Field

from src.internal.biz.entities.response.base import BaseResponseModel


class LessonFileSimpleResponse(BaseResponseModel):
    name: str = Field(..., example='Название файла')
    file_link: str = Field(..., example='https://...')
