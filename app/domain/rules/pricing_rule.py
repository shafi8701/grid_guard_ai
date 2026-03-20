from app.domain.rules.base_rule import BaseRule
from app.domain.models.rule_result import RuleResult


class PricingRule(BaseRule):

    def evaluate(self, request) -> RuleResult:

        if request.price < 100:
            return RuleResult(
                blocked=False,
                reason="Price unusually low",
                conditions=["Verify pricing compliance"]
            )

        return RuleResult(blocked=False)