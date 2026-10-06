def process_incident(data):
    return {
        "incident": data["incident"].strip(),
        "service": data["service"].strip(),
        "environment": data["environment"],
        "affected_users": int(data["affected_users"]),
        "duration": int(data["duration"]),
        "business_impact": data["business_impact"]
    }