
from db.session import get_results as _get_results, get_target_risk_score

def get_results():
    return _get_results()

def get_target_risk(target):
    return {"target": target, "risk_score": get_target_risk_score(target)}
