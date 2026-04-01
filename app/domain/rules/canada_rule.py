from domain.rules.base_rule import BaseRule
from domain.models.rule_result import RuleResult


class CanadaRule(BaseRule):

    def evaluate(self, request) -> RuleResult:

        if "canada" in request.region.lower():
            certs = [c.upper() for c in request.certifications]

            if "CSA" not in certs:
                return RuleResult(
                    blocked=True,
                    reason="CSA certification required in Canada",
                    conditions=["CSA certification mandatory"]
                )

        return RuleResult(blocked=False)