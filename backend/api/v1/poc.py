
from fastapi import APIRouter
from services.schemas import PocRequest
from services.poc_service import run_poc

router = APIRouter()

@router.post("/generate-poc")
def generate(req: PocRequest):
    return run_poc(req)
