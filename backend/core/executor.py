
import time, requests

def execute(target):
    score = 0
    start = time.time()
    try:
        r = requests.get(target, timeout=8)
        if time.time() - start > 6:
            score += 40
        if r.status_code >= 500:
            score += 30
    except requests.exceptions.Timeout:
        score += 40
    except:
        score += 20

    if score >= 70:
        return {"status": "CONFIRMED", "confidence": "HIGH"}
    if score >= 40:
        return {"status": "POSSIBLE", "confidence": "MEDIUM"}
    return {"status": "NOT CONFIRMED", "confidence": "LOW"}
