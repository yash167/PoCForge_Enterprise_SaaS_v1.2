
from fastapi import FastAPI
from api.v1 import health, cves, poc, results, export
from db.session import init_db

init_db()
app = FastAPI(title="PoCForge Enterprise", version="1.1")

app.include_router(health.router, prefix="/api/v1")
app.include_router(cves.router, prefix="/api/v1")
app.include_router(poc.router, prefix="/api/v1")
app.include_router(results.router, prefix="/api/v1")
app.include_router(export.router, prefix="/api/v1")
