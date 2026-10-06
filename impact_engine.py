def assess_impact(data):

    users = data["affected_users"]
    duration = data["duration"]
    business_impact = data["business_impact"]

    if users >= 1000 or business_impact == "Critical":
        level = "CRITICAL"

    elif users >= 500 or duration >= 60 or business_impact == "High":
        level = "HIGH"

    elif users >= 100 or duration >= 30 or business_impact == "Medium":
        level = "MEDIUM"

    else:
        level = "LOW"

    return {
        "impact_level": level,
        "affected_users": users,
        "duration": duration
    }