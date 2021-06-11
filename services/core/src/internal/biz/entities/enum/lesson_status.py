from enum import Enum


class LessonStatusEnum(str, Enum):
    published = 'published'
    draft = 'draft'
    archive = 'archive'
