from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
async def tester():
    return [{"result": "test"}]