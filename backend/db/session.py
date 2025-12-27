
import sqlite3
DB = "pocforge.db"

def _c():
    return sqlite3.connect(DB)

def init_db():
    c = _c()
    c.execute("CREATE TABLE IF NOT EXISTS cves (id TEXT, severity REAL, description TEXT, published TEXT)")
    c.execute("""CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cve TEXT,
        target TEXT,
        status TEXT,
        confidence TEXT,
        executed_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )""")
    c.commit(); c.close()

def add_cve(i,s,d,p):
    c=_c(); c.execute("INSERT INTO cves VALUES (?,?,?,?)",(i,s,d,p)); c.commit(); c.close()

def get_cves(min_sev):
    c=_c()
    rows=c.execute("SELECT id,severity,description,published FROM cves WHERE severity>=? ORDER BY published DESC",(min_sev,)).fetchall()
    c.close()
    return [{"cve":r[0],"severity":r[1],"description":r[2],"published":r[3]} for r in rows]

def add_result(cve,target,res):
    c=_c()
    c.execute("INSERT INTO results (cve,target,status,confidence) VALUES (?,?,?,?)",
              (cve,target,res["status"],res["confidence"]))
    c.commit(); c.close()

def get_results():
    c=_c()
    rows=c.execute("SELECT cve,target,status,confidence,executed_at FROM results ORDER BY executed_at DESC").fetchall()
    c.close()
    return [{"cve":r[0],"target":r[1],"status":r[2],"confidence":r[3],"timestamp":r[4]} for r in rows]

def get_target_risk_score(target):
    c=_c()
    rows=c.execute("SELECT confidence FROM results WHERE target=?",(target,)).fetchall()
    c.close()
    score = 0
    for r in rows:
        if r[0]=="HIGH": score+=10
        elif r[0]=="MEDIUM": score+=5
        elif r[0]=="LOW": score+=1
    return score
