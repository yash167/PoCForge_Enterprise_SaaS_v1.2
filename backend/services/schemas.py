
from pydantic import BaseModel

class PocRequest(BaseModel):
    cve_id: str
    target: str
