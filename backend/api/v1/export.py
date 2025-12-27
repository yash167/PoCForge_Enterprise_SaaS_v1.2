
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from services.export_service import export_csv

router = APIRouter()

@router.get("/export/csv")
def export():
    return StreamingResponse(
        export_csv(),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=pocforge_results.csv"}
    )
