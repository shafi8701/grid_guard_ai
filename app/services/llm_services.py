from domain.models.request import ComplianceRequest


def get_llm_response(request: ComplianceRequest):
    """
    Placeholder for fine-tuned model
    """

    return {
        "allowed": True,
        "region": request.region,
        "conditions": ["NEC compliance required"],
        "pricing_compliance": "VALID",
        "risk_level": "LOW"
    }