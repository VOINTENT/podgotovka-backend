from fastapi import APIRouter

test_router = APIRouter(prefix='/test')


@test_router.get('')
async def test():
    return True
