from app.models.request import ComplianceRequest


def check_rules(request: ComplianceRequest):
    
    region = request.region.lower()
    certs = [c.upper() for c in request.certifications]

    # Canada → CSA required
    if "canada" in region:
        if "CSA" not in certs:
            return {
                "blocked": True,
                "response": {
                    "allowed": False,
                    "region": request.region,
                    "reason": "CSA certification required in Canada",
                    "conditions": ["CSA certification mandatory"],
                    "risk_level": "HIGH"
                }
            }

    # USA → UL required
    if "usa" in region or "california" in region or "texas" in region:
        if "UL" not in certs:
            return {
                "blocked": True,
                "response": {
                    "allowed": False,
                    "region": request.region,
                    "reason": "UL certification required in USA",
                    "conditions": ["UL certification mandatory"],
                    "risk_level": "HIGH"
                }
            }

    return {"blocked": False}