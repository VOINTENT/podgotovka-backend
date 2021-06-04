from fastapi import APIRouter

from src.internal.servers.http.api.teach.accounts import accounts_router

teach_router = APIRouter(prefix='/teach')

teach_router.include_router(accounts_router)
