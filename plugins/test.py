""" example plugin to extend a /test route """
from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
async def tester():
    """ test route """
    return [{"result": "test"}]
