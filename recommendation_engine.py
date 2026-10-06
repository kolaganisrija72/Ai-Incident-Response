def generate_recommendations(
    data,
    severity,
    risk,
    decision
):

    recommendations = []

    if risk["risk_score"] >= 80:
        recommendations.append(
            "Immediately escalate the incident to the responsible technical team."
        )

    if data["environment"] == "Production":
        recommendations.append(
            "Prioritize investigation because the incident affects production."
        )

    recommendations.append(
        "Review application, infrastructure and service logs."
    )

    recommendations.append(
        "Identify the technical root cause before applying permanent changes."
    )

    recommendations.append(
        "Monitor the affected service after recovery."
    )

    if data["affected_users"] >= 1000:
        recommendations.append(
            "Evaluate business impact and communicate with stakeholders."
        )

    return recommendations