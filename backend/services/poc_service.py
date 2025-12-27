
from core.executor import execute
from db.session import add_result

def run_poc(req):
    result = execute(req.target)
    add_result(req.cve_id, req.target, result)
    return result
