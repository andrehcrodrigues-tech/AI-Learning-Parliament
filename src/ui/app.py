import streamlit as st

st.set_page_config(page_title="AI Learning Parliament", layout="wide")

st.title("AI Learning Parliament")
st.caption("Multi-agent reasoning system for certification readiness")

role = st.text_input("Role", "Cloud Engineer")
certification = st.text_input("Target Certification", "AI-102")
skills = st.text_area("Current Skills", "Azure basics, Python, API development")
hours = st.number_input("Available Study Hours per Week", min_value=1, max_value=20, value=4)
workload = st.text_area("Workload Signals", "21 meeting hours/week, 8 focus hours/week")
career_goal = st.text_input("Career Goal", "Move into AI Engineering")
team_goal = st.text_input("Team Goal", "Increase GenAI delivery capability within 3 months")

if st.button("Generate Certification Readiness Report"):
    st.info("Connect this button to the Microsoft Foundry Workflow endpoint.")
    st.markdown("""
    ## Demo Payload

    This Streamlit UI is a lightweight optional wrapper for the Foundry workflow.
    """)
