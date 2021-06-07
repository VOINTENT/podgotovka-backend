from typing import Optional

from fastapi import Query


class PaginationParams:
    def __init__(self, limit: Optional[int] = Query(100, ge=0, le=100), skip: Optional[int] = Query(0, ge=0)) -> None:
        self.limit = limit
        self.skip = skip
