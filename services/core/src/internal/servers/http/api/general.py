from fastapi import APIRouter

from src.extra.entities.response.exceptions.base import ExceptionResponse
from src.internal.servers.http.api.test import test_router

general_router = APIRouter(prefix='/core/v1', responses={400: {'model': ExceptionResponse},
                                                         500: {'model': ExceptionResponse}})
general_router.include_router(test_router)
