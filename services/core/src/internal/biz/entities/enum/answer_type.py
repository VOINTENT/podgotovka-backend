from src.internal.biz.entities.response.base import BaseResponseModel


class AnswerTypeEnum(BaseResponseModel):
    one = 'one'
    many = 'many'
    text = 'text'
