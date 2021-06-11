from typing import Optional

from pydantic.fields import Field

from src.internal.biz.entities.response.base import BaseResponseModel


class AccountTeacherDetailResponse(BaseResponseModel):
    id: int = Field(..., example=1)
    email: str = Field(..., example="mail@mail.com")
    name: str = Field(..., example="Иван")
    last_name: Optional[str] = Field(None, example="IV")
    middle_name: Optional[str] = Field(None, example="Васильевич")
    photo_link: Optional[str] = Field(None, example="https://...")
    description: Optional[str] = Field(None, example="Грозный. Поменял профессию")
