
from fastapi import APIRouter
from services.result_service import get_results, get_target_risk

router = APIRouter()

@router.get("/results")
def results():
    return get_results()

@router.get("/risk/{target}")
def risk(target: str):
    return get_target_risk(target)
