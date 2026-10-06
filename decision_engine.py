def make_decision(risk, severity):

    score = risk["risk_score"]

    if score >= 80 or severity["severity_level"] == "CRITICAL":
        decision = "IMMEDIATE ESCALATION"

    elif score >= 60:
        decision = "MANUAL INCIDENT REVIEW"

    elif score >= 30:
        decision = "VERIFY AND MONITOR"

    else:
        decision = "NORMAL MONITORING"

    return {
        "decision": decision
    }