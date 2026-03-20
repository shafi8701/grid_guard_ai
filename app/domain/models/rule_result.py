class RuleResult:
    def __init__(self, blocked: bool, reason=None, conditions=None):
        self.blocked = blocked
        self.reason = reason
        self.conditions = conditions or []