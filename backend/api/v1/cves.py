
from fastapi import APIRouter, BackgroundTasks, Query
from services.cve_service import sync_cves, list_cves

router = APIRouter()

@router.post("/sync-cves")
def sync(background: BackgroundTasks):
    background.add_task(sync_cves)
    return {"message": "CVE sync started"}

@router.get("/cves")
def get_cves(min_severity: float = Query(0)):
    return list_cves(min_severity)
