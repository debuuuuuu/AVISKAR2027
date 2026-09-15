from src.data_models import Task, RiskTier, RiskAssessment, VerificationMode


class RiskAssessmentLayer:
    """
    Risk Assessment Layer.
    Maps task stakes to numerical risk scores and mandatory confidence gates.
    """

    def __init__(self, base_threshold: float = 0.50):
        self.base_threshold = base_threshold

    def assess(self, task: Task) -> RiskAssessment:
        if task.risk_level == RiskTier.LOW:
            risk_score = 0.20
            conf_threshold = 0.50
            min_omega = 0.20
            mode = VerificationMode.SCHEMA
        elif task.risk_level == RiskTier.MEDIUM:
            risk_score = 0.50
            conf_threshold = 0.75
            min_omega = 0.50
            mode = VerificationMode.DETERMINISTIC
        elif task.risk_level == RiskTier.HIGH:
            risk_score = 0.85
            conf_threshold = 0.88
            min_omega = 0.70
            mode = VerificationMode.DETERMINISTIC
        else:  # CRITICAL
            risk_score = 0.95
            conf_threshold = 0.95
            min_omega = 0.85
            mode = VerificationMode.DETERMINISTIC

        return RiskAssessment(
            task_id=task.task_id,
            risk_tier=task.risk_level,
            risk_score=risk_score,
            confidence_threshold=conf_threshold,
            min_evidence_confidence=min_omega,
            mandatory_verification_mode=mode
        )
