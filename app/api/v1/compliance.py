from fastapi import APIRouter
from domain.models.request import ComplianceRequest
from domain.models.response import ComplianceResponse
from services.compliance_service import evaluate_compliance

router = APIRouter(prefix="/v1/compliance", tags=["Compliance"])

@router.post("/check", response_model=ComplianceResponse)
def check_compliance(request: ComplianceRequest):
    return evaluate_compliance(request)