from src.internal.biz.creators.base import Creator
from src.internal.biz.entities.response.common.just_id import JustIdResponse


class JustIdResponseCreator(Creator):
    @staticmethod
    def get_from_id(id: int) -> JustIdResponse:
        return JustIdResponse(id=id)
