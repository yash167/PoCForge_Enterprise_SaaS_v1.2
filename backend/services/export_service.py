
from db.session import get_results
import csv, io

def export_csv():
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["CVE","Target","Status","Confidence","Timestamp"])
    for r in get_results():
        writer.writerow([r["cve"], r["target"], r["status"], r["confidence"], r["timestamp"]])
    output.seek(0)
    return output
