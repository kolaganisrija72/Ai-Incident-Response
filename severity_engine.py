def calculate_severity(data):

    score = 0

    users = data["affected_users"]
    duration = data["duration"]
    environment = data["environment"]
    impact = data["business_impact"]

    if users >= 5000:
        score += 40

    elif users >= 1000:
        score += 30

    elif users >= 500:
        score += 20

    elif users >= 100:
        score += 10

    if duration >= 120:
        score += 25

    elif duration >= 60:
        score += 20

    elif duration >= 30:
        score += 15

    elif duration >= 10:
        score += 10

    if environment == "Production":
        score += 20

    elif environment == "Staging":
        score += 10

    impact_scores = {
        "Critical": 20,
        "High": 15,
        "Medium": 10,
        "Low": 5
    }

    score += impact_scores.get(impact, 0)

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
        "severity_score": score,
        "severity_level": level
    }