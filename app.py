import streamlit as st
import json
from datetime import datetime

from incident_processor import process_incident
from backend.ai_analyzer import analyze_incident as backend_analyze_incident
from backend.severity_engine import calculate_severity
from backend.root_cause_engine import find_root_cause
from backend.impact_engine import assess_impact
from backend.risk_engine import calculate_risk
from backend.decision_engine import make_decision
from backend.recommendation_engine import generate_recommendations


st.set_page_config(
    page_title="AI Incident Response",
    page_icon="🚨",
    layout="wide"
)


with open(
    "frontend/style.css",
    "r",
    encoding="utf-8"
) as f:

    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )


if "result" not in st.session_state:
    st.session_state.result = None


st.sidebar.title(
    "🚨 AI Incident Response"
)

st.sidebar.markdown("---")


page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "📝 Incident Input",
        "🤖 AI Analysis",
        "🔥 Severity Analysis",
        "🔍 Root Cause Analysis",
        "💥 Impact Assessment",
        "⚠️ Risk Assessment",
        "🧠 Decision Intelligence",
        "💡 Recommendations",
        "📊 Analytics",
        "📑 Incident Report"
    ]
)


st.sidebar.markdown("---")

st.sidebar.info(
    "AI-powered incident response "
    "and decision intelligence."
)


def analyze_full_incident(
    incident,
    service,
    environment,
    users,
    duration,
    business_impact
):

    data = {

        "incident": incident,

        "service": service,

        "environment": environment,

        "affected_users": users,

        "duration": duration,

        "business_impact": business_impact
    }


    processed = process_incident(data)


    ai = backend_analyze_incident(
        processed
    )


    severity = calculate_severity(
        processed
    )


    root_cause = find_root_cause(
        processed
    )


    impact = assess_impact(
        processed
    )


    risk = calculate_risk(
        processed,
        severity,
        impact
    )


    decision = make_decision(
        risk,
        severity
    )


    recommendations = generate_recommendations(
        processed,
        severity,
        risk,
        decision
    )


    return {

        "timestamp":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

        "incident":
            processed,

        "ai_analysis":
            ai,

        "severity":
            severity,

        "root_cause":
            root_cause,

        "impact":
            impact,

        "risk":
            risk,

        "decision":
            decision,

        "recommendations":
            recommendations
    }


# ------------------------------------------------
# DASHBOARD
# ------------------------------------------------

if page == "🏠 Dashboard":

    st.title(
        "🚨 AI Autonomous Incident Response "
        "& Decision Intelligence"
    )

    st.write(
        "Intelligent incident analysis, "
        "risk assessment and automated "
        "decision support."
    )

    st.divider()


    result = st.session_state.result


    if result:

        severity = result[
            "severity"
        ]["severity_level"]

        risk = result[
            "risk"
        ]["risk_score"]

        decision = result[
            "decision"
        ]["decision"]

    else:

        severity = "NOT ANALYZED"

        risk = 0

        decision = "NO DECISION"


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "🚨 Incidents",
            "1" if result else "0"
        )


    with col2:

        st.metric(
            "🔥 Severity",
            severity
        )


    with col3:

        st.metric(
            "⚠️ Risk Score",
            f"{risk}/100"
        )


    with col4:

        st.metric(
            "🧠 Decision",
            decision
        )


    st.divider()


    st.subheader(
        "🔄 Incident Response Workflow"
    )


    steps = [

        "📝 Incident Input",

        "🤖 AI Analysis",

        "🔥 Severity Analysis",

        "🔍 Root Cause",

        "💥 Impact Assessment",

        "⚠️ Risk Assessment",

        "🧠 Decision Intelligence",

        "💡 Recommendations"
    ]


    for i in range(
        0,
        len(steps),
        4
    ):

        cols = st.columns(4)

        for j, col in enumerate(cols):

            if i + j < len(steps):

                with col:

                    st.info(
                        steps[i + j]
                    )


# ------------------------------------------------
# INCIDENT INPUT
# ------------------------------------------------

elif page == "📝 Incident Input":

    st.title(
        "📝 Incident Input"
    )


    incident = st.text_area(

        "Incident Description",

        placeholder=(
            "Example: Payment server is down "
            "and customers cannot complete payments."
        ),

        height=150
    )


    col1, col2 = st.columns(2)


    with col1:

        service = st.text_input(
            "Affected Service",
            "Payment Gateway"
        )


        environment = st.selectbox(

            "Environment",

            [
                "Production",
                "Staging",
                "Development"
            ]
        )


        users = st.number_input(

            "Affected Users",

            min_value=0,

            value=100,

            step=100
        )


    with col2:

        duration = st.number_input(

            "Duration (minutes)",

            min_value=0,

            value=30,

            step=10
        )


        business_impact = st.selectbox(

            "Business Impact",

            [
                "Critical",
                "High",
                "Medium",
                "Low"
            ]
        )


    st.divider()


    if st.button(
        "🚀 Analyze Incident",
        use_container_width=True
    ):

        if not incident.strip():

            st.error(
                "Please enter an incident description."
            )

        else:

            st.session_state.result = (
                analyze_full_incident(

                    incident,

                    service,

                    environment,

                    users,

                    duration,

                    business_impact
                )
            )


            st.success(
                "Incident analyzed successfully!"
            )


# ------------------------------------------------
# AI ANALYSIS
# ------------------------------------------------

elif page == "🤖 AI Analysis":

    st.title(
        "🤖 AI Analysis"
    )


    if not st.session_state.result:

        st.warning(
            "Please analyze an incident first."
        )

    else:

        ai = st.session_state.result[
            "ai_analysis"
        ]


        col1, col2 = st.columns(2)


        with col1:

            st.subheader(
                "Incident Type"
            )

            st.info(
                ai["incident_type"]
            )


        with col2:

            st.subheader(
                "Priority"
            )

            st.warning(
                ai["priority"]
            )


# ------------------------------------------------
# SEVERITY
# ------------------------------------------------

elif page == "🔥 Severity Analysis":

    st.title(
        "🔥 Severity Analysis"
    )


    if not st.session_state.result:

        st.warning(
            "Analyze an incident first."
        )

    else:

        data = st.session_state.result[
            "severity"
        ]


        col1, col2 = st.columns(2)


        with col1:

            st.metric(

                "Severity Score",

                f"{data['severity_score']}/100"
            )


        with col2:

            st.metric(

                "Severity Level",

                data["severity_level"]
            )


# ------------------------------------------------
# ROOT CAUSE
# ------------------------------------------------

elif page == "🔍 Root Cause Analysis":

    st.title(
        "🔍 Root Cause Analysis"
    )


    if not st.session_state.result:

        st.warning(
            "Analyze an incident first."
        )

    else:

        st.subheader(
            "Probable Root Cause"
        )


        st.info(
            st.session_state.result[
                "root_cause"
            ]
        )


        st.caption(
            "This is an AI-assisted preliminary "
            "assessment. System logs should be "
            "reviewed for confirmation."
        )


# ------------------------------------------------
# IMPACT
# ------------------------------------------------

elif page == "💥 Impact Assessment":

    st.title(
        "💥 Impact Assessment"
    )


    if not st.session_state.result:

        st.warning(
            "Analyze an incident first."
        )

    else:

        data = st.session_state.result[
            "impact"
        ]


        col1, col2 = st.columns(2)


        with col1:

            st.metric(
                "Impact Level",
                data["impact_level"]
            )


        with col2:

            st.metric(
                "Affected Users",
                data["affected_users"]
            )


        st.write(
            f"Incident duration: "
            f"{data['duration']} minutes"
        )


# ------------------------------------------------
# RISK
# ------------------------------------------------

elif page == "⚠️ Risk Assessment":

    st.title(
        "⚠️ Risk Assessment"
    )


    if not st.session_state.result:

        st.warning(
            "Analyze an incident first."
        )

    else:

        data = st.session_state.result[
            "risk"
        ]


        st.metric(
            "Risk Score",
            f"{data['risk_score']}/100"
        )


        st.progress(
            data["risk_score"] / 100
        )


        if data["risk_level"] == "CRITICAL":

            st.error(
                "🚨 CRITICAL RISK"
            )

        elif data["risk_level"] == "HIGH":

            st.warning(
                "⚠️ HIGH RISK"
            )

        elif data["risk_level"] == "MEDIUM":

            st.info(
                "🟡 MEDIUM RISK"
            )

        else:

            st.success(
                "🟢 LOW RISK"
            )


# ------------------------------------------------
# DECISION
# ------------------------------------------------

elif page == "🧠 Decision Intelligence":

    st.title(
        "🧠 Decision Intelligence"
    )


    if not st.session_state.result:

        st.warning(
            "Analyze an incident first."
        )

    else:

        decision = st.session_state.result[
            "decision"
        ]


        st.success(
            f"🧠 {decision['decision']}"
        )


        st.write(
            "This recommendation is generated "
            "using the incident's severity "
            "and risk assessment."
        )


# ------------------------------------------------
# RECOMMENDATIONS
# ------------------------------------------------

elif page == "💡 Recommendations":

    st.title(
        "💡 Response Recommendations"
    )


    if not st.session_state.result:

        st.warning(
            "Analyze an incident first."
        )

    else:

        recommendations = (
            st.session_state.result[
                "recommendations"
            ]
        )


        for i, item in enumerate(
            recommendations,
            1
        ):

            st.info(
                f"{i}. {item}"
            )


# ------------------------------------------------
# ANALYTICS
# ------------------------------------------------

elif page == "📊 Analytics":

    st.title(
        "📊 Incident Analytics"
    )


    if not st.session_state.result:

        st.info(
            "Analyze an incident "
            "to generate analytics."
        )

    else:

        result = (
            st.session_state.result
        )


        chart_data = {

            "Score": [

                result["severity"][
                    "severity_score"
                ],

                result["risk"][
                    "risk_score"
                ]
            ]
        }


        st.bar_chart(
            chart_data
        )


        st.write(
            "The chart compares severity "
            "and risk scores."
        )


# ------------------------------------------------
# INCIDENT REPORT
# ------------------------------------------------

elif page == "📑 Incident Report":

    st.title(
        "📑 Incident Report"
    )


    if not st.session_state.result:

        st.warning(
            "Analyze an incident first."
        )

    else:

        result = (
            st.session_state.result
        )


        st.subheader(
            "Incident"
        )

        st.write(
            result["incident"]["incident"]
        )


        st.subheader(
            "AI Analysis"
        )

        st.write(
            result["ai_analysis"][
                "incident_type"
            ]
        )


        st.write(
            f"Priority: "
            f"{result['ai_analysis']['priority']}"
        )


        st.subheader(
            "Severity"
        )

        st.write(

            f"{result['severity']['severity_level']} "
            f"("
            f"{result['severity']['severity_score']}"
            f"/100)"
        )


        st.subheader(
            "Root Cause"
        )

        st.write(
            result["root_cause"]
        )


        st.subheader(
            "Impact"
        )

        st.write(
            result["impact"]["impact_level"]
        )


        st.subheader(
            "Risk"
        )

        st.write(

            f"{result['risk']['risk_level']} "
            f"("
            f"{result['risk']['risk_score']}"
            f"/100)"
        )


        st.subheader(
            "Decision"
        )

        st.success(
            result["decision"]["decision"]
        )


        st.subheader(
            "Recommendations"
        )


        for item in result[
            "recommendations"
        ]:

            st.write(
                f"• {item}"
            )


        report = json.dumps(
            result,
            indent=4
        )


        st.download_button(

            "📥 Download Incident Report",

            report,

            "incident_report.json",

            "application/json"
        )
