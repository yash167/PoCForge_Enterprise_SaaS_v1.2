
import requests, time
from db.session import add_cve, get_cves

NVD = "https://services.nvd.nist.gov/rest/json/cves/2.0"
HEADERS = {"User-Agent": "PoCForge"}

def extract_severity(metrics):
    for k in ("cvssMetricV31","cvssMetricV30","cvssMetricV2"):
        if k in metrics:
            return metrics[k][0]["cvssData"]["baseScore"]
    return 0.0

def sync_cves():
    params = {
        "pubStartDate": "2023-01-01T00:00:00.000Z",
        "pubEndDate": "2025-12-31T23:59:59.999Z",
        "resultsPerPage": 50
    }
    data = requests.get(NVD, params=params, headers=HEADERS).json()
    vulns = sorted(
        data.get("vulnerabilities", []),
        key=lambda x: x["cve"]["published"],
        reverse=True
    )

    for v in vulns:
        cve = v["cve"]
        add_cve(
            cve["id"],
            extract_severity(cve.get("metrics", {})),
            cve["descriptions"][0]["value"],
            cve["published"]
        )
        time.sleep(2)

def list_cves(min_sev):
    return get_cves(min_sev)
