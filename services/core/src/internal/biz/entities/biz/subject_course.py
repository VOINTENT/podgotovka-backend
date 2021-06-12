from typing import Optional


class SubjectCourse:
    def __init__(self,
                 name: Optional[str] = None,
                 subject_id: Optional[int] = None,
                 course_id: Optional[int] = None) -> None:
        self.name = name
        self.subject_id = subject_id
        self.course_id = course_id
