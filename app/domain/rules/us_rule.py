from app.domain.rules.base_rule import BaseRule
from app.domain.models.rule_result import RuleResult


class USRule(BaseRule):

    def evaluate(self, request) -> RuleResult:

        region = request.region.lower()
        certs = [c.upper() for c in request.certifications]

        if any(r in region for r in ["usa", "california", "texas"]):
            if "UL" not in certs:
                return RuleResult(
                    blocked=True,
                    reason="UL certification required in USA",
                    conditions=["UL certification mandatory"]
                )

        return RuleResult(blocked=False)