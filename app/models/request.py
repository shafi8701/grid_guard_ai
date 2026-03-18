from pydantic import BaseModel, Field
from typing import List

class ComplianceRequest(BaseModel):
    product: str = Field(..., example="EV Charger")
    region: str = Field(..., example="California, USA")
    price: float = Field(..., gt=0)
    certifications: List[str] = Field(default_factory=list)