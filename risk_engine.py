def calculate_risk(data, severity, impact):

    score = severity["severity_score"]

    if impact["impact_level"] == "CRITICAL":
        score += 10

    elif impact["impact_level"] == "HIGH":
        score += 7

    elif impact["impact_level"] == "MEDIUM":
        score += 4

    if data["environment"] == "Production":
        score += 5

    score = min(score, 100)

    if score >= 80:
        level = "CRITICAL"

    elif score >= 60:
        level = "HIGH"

    elif score >= 30:
        level = "MEDIUM"

    else:
        level = "LOW"

    return {
        "risk_score": score,
        "risk_level": level
    }