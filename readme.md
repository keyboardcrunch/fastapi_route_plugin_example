# FastAPI Route Plugin Framework

This repository contains a working example for automatically importing 'plugins' to extend FastAPI routes.

## Usage

You can extend main.py however you choose, but plugin files can be named anything but must have a FastAPI *APIRouter()* defined as *router*.
```
from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
async def tester():
    return [{"result": "test"}]
```

To run the sample:
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

**Routes:**
* http://127.0.0.1:8000/
* http://127.0.0.1:8000/test
