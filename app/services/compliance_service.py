from app.services.rule_engine import RuleEngine
from app.mappers.response_mapper import map_rule_to_response
from app.services.llm_service import get_llm_response
from app.domain.models.response import ComplianceResponse

rule_engine = RuleEngine()

def evaluate_compliance(request):

    # Step 1: Rule evaluation
    rule_result = rule_engine.evaluate(request)

    if rule_result.blocked:
        return map_rule_to_response(rule_result, request)

    # Step 2: LLM
    llm_result = get_llm_response(request)

    return ComplianceResponse(**llm_result)