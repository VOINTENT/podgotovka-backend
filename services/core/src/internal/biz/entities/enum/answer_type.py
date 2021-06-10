from enum import Enum


class AnswerTypeEnum(str, Enum):
    one = 'one'
    many = 'many'
    text = 'text'
