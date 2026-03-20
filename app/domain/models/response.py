from pydantic import BaseModel
from typing import List, Optional

class ComplianceResponse(BaseModel):
    allowed: bool
    region: str
    conditions: List[str] = []
    reason: Optional[str] = None
    pricing_compliance: Optional[str] = None
    risk_level: str