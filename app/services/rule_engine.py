from domain.rules.canada_rule import CanadaRule
from domain.rules.us_rule import USRule
from domain.rules.pricing_rule import PricingRule
from domain.models.rule_result import RuleResult


class RuleEngine:

    def __init__(self):
        self.rules = [
            CanadaRule(),
            USRule(),
            PricingRule()
        ]

    def evaluate(self, request) -> RuleResult:

        for rule in self.rules:
            result = rule.evaluate(request)

            # Stop immediately if blocked
            if result.blocked:
                return result

        # Default: allowed
        return RuleResult(blocked=False)