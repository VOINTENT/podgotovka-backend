from fastapi import APIRouter

from src.extra.entities.response.exceptions.base import ExceptionResponse
from src.internal.servers.http.api.admin.general import admin_router
from src.internal.servers.http.api.edu.general import edu_router
from src.internal.servers.http.api.teach.general import teach_router

general_router = APIRouter(prefix='/core/v1', responses={400: {'model': ExceptionResponse},
                                                         500: {'model': ExceptionResponse}})
general_router.include_router(edu_router)
general_router.include_router(teach_router)
general_router.include_router(admin_router)
