from services.rule_engine import RuleEngine
from mappers.response_mapper import map_rule_to_response
from services.llm_services import get_llm_response
from domain.models.response import ComplianceResponse

#Logging framework imports
from logging_framework import get_request_logger
from logging_framework.log_context import LogContext, set_context, add_to_context
import uuid
#########

rule_engine = RuleEngine()

def evaluate_compliance(request):

    # Create a context for this request
    ctx = LogContext()
    ctx.set_request_id(str(uuid.uuid4()))
    set_context(ctx)
    
    # Get the logger (no arguments required)
    logger = get_request_logger()

    logger.info("Evaluating compliance processing")


    # Step 1: Rule evaluation
    rule_result = rule_engine.evaluate(request)

    if rule_result.blocked:
        return map_rule_to_response(rule_result, request)

    # Step 2: LLM
    llm_result = get_llm_response(request)

    return ComplianceResponse(**llm_result)