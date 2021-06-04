from src.internal.biz.creators.biz.token import Token
from src.internal.biz.entities.response.account.token import TokenResponse


class TokenResponseCreator:
    @staticmethod
    def get_from_token(token: Token) -> TokenResponse:
        return TokenResponse(
            access_token=token.auth_token,
            token_type=Token.token_type
        )
