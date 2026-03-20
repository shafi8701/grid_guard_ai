from abc import ABC, abstractmethod
from app.domain.models.rule_result import RuleResult


class BaseRule(ABC):

    @abstractmethod
    def evaluate(self, request) -> RuleResult:
        pass