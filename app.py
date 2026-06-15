import streamlit as st

from database.db import (
    create_tables,
    save_skill_level,
    load_skill_level
)

from modules import query
from modules import code_generator
from modules import error_detector
from modules import code_explainer
from modules import practice

# Create database tables
create_tables()

st.set_page_config(
    page_title="AI Coding Assistant",
    page_icon="🤖",
    layout="wide"
)

# Load saved skill level
if "skill_level" not in st.session_state:
    st.session_state.skill_level = load_skill_level()

# Header
st.title("🤖 AI Coding Assistant")
st.caption("Learn • Practice • Build • Improve")

# Sidebar
with st.sidebar:

    st.header("🎯 Adaptive Learning")

    level = st.selectbox(
        "Select Your Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ],
        index=[
            "Beginner",
            "Intermediate",
            "Advanced"
        ].index(st.session_state.skill_level)
    )

    if level != st.session_state.skill_level:
        st.session_state.skill_level = level
        save_skill_level(level)

    st.success(f"Current Level: {level}")

    st.divider()

    page = st.radio(
        "📚 Select Module",
        [
            "Query Interface",
            "Code Generator",
            "Error Detector",
            "Code Explainer",
            "Practice Problems"
        ]
    )

# Main Content Area

if page == "Query Interface":
    query.run()

elif page == "Code Generator":
    code_generator.run()

elif page == "Error Detector":
    error_detector.run()

elif page == "Code Explainer":
    code_explainer.run()

elif page == "Practice Problems":
    practice.run()