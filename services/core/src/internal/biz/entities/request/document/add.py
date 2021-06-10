from pydantic import Field

from src.internal.biz.entities.request.base import BaseRequestModel


class DocumentAddRequest(BaseRequestModel):
    name: str = Field(..., example='Название файла')
    file_link: str = Field(..., example='https://...')
