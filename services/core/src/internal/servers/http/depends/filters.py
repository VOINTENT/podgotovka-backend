from datetime import datetime
from typing import Optional

from fastapi import Query

from src.internal.biz.entities.enum.order import OrderEnum


def get_date_start(date_start: Optional[int] = Query(None, ge=1, le=90_000_000_000)) -> datetime:
    return datetime.fromtimestamp(date_start) if date_start else None


def get_date_finish(date_finish: Optional[int] = Query(None, ge=1, le=90_000_000_000)) -> datetime:
    return datetime.fromtimestamp(date_finish) if date_finish else None


def get_order(order: Optional[OrderEnum] = Query(OrderEnum.asc)):
    return order


def get_course_id(course_id: Optional[int] = Query(None)):
    return course_id


def get_subject_id(subject_id: Optional[int] = Query(None)):
    return subject_id


def get_search(search: Optional[str] = Query(None)):
    return search.lower() if search else None
