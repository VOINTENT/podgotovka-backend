from src.internal.biz.entities.response.base import BaseResponseModel


class TokenResponse(BaseResponseModel):
    access_token: str
    token_type: str
