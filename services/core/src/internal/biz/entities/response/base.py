from pydantic import BaseModel, Extra


class BaseResponseModel(BaseModel):
    class Config:
        extra = Extra.forbid
        validate_assignment = True
        use_enum_values = True
