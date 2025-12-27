
# PoCForge Enterprise

Enterprise-grade CVE PoC validation platform.

## Features
- CVE Sync (2023–2025)
- Latest-first sorting
- Safe PoC execution
- Result history
- Per-target risk scoring
- CSV export

## Run
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
