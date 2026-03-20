from app.schemas.response import ComplianceResponse


def map_rule_to_response(rule_result, request):

    return ComplianceResponse(
        allowed=not rule_result.blocked,
        region=request.region,
        reason=rule_result.reason,
        conditions=rule_result.conditions,
        risk_level="HIGH" if rule_result.blocked else "LOW"
    )