def analyze_incident(data):

    text = (
        data["incident"] + " " +
        data["service"] + " " +
        data["business_impact"]
    ).lower()

    if any(x in text for x in ["database", "sql", "mysql", "postgres"]):
        incident_type = "Database Incident"

    elif any(x in text for x in ["payment", "transaction", "gateway"]):
        incident_type = "Payment Service Incident"

    elif any(x in text for x in ["network", "connection", "timeout"]):
        incident_type = "Network Incident"

    elif any(x in text for x in ["server", "cpu", "memory"]):
        incident_type = "Server Infrastructure Incident"

    elif any(x in text for x in ["security", "attack", "malware", "unauthorized"]):
        incident_type = "Security Incident"

    elif any(x in text for x in ["application", "website", "app"]):
        incident_type = "Application Incident"

    else:
        incident_type = "General IT Incident"

    if data["environment"] == "Production":
        priority = "High"
    else:
        priority = "Normal"

    return {
        "incident_type": incident_type,
        "priority": priority
    }