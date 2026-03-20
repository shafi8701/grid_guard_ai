from fastapi import APIRouter
from app.domain.models.request import ComplianceRequest
from app.domain.models.response import ComplianceResponse
from app.services.compliance_service import evaluate_compliance

router = APIRouter(prefix="/v1/compliance", tags=["Compliance"])

@router.post("/check", response_model=ComplianceResponse)
def check_compliance(request: ComplianceRequest):
    return evaluate_compliance(request)