from pydantic import BaseModel


class BaseRequestModel(BaseModel):
    class Config:
        validate_assignment = True
        use_enum_values = True
