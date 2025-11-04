"""MLPerf Inference Dashboard - Standalone Application.

This dashboard provides comprehensive analysis and visualization of MLPerf Inference
benchmark results across multiple versions (v4.1, v5.0, v5.1).
"""

import streamlit as st

# Import styling first
from dashboard_styles import apply_theme_css, inject_mlperf_css

# Import MLPerf dashboard functionality
from mlperf_datacenter import render_mlperf_dashboard

# Page configuration
st.set_page_config(
    page_title="MLPerf Inference Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize session state for theme if not exists
if "theme_mode" not in st.session_state:
    st.session_state.theme_mode = "auto"

# Apply theme-specific CSS
apply_theme_css()

# Inject custom CSS
inject_mlperf_css()

# Header with theme toggle
col1, col2 = st.columns([7, 1])

with col1:
    st.markdown(
        "<h1 style='text-align: center;'>📊 MLPerf Dashboard</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div style='text-align: center;'>
        <strong>Comprehensive analysis of MLPerf Inference benchmark results</strong><br>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    # Theme toggle button
    current_mode = st.session_state.get("theme_mode", "auto")

    if current_mode == "auto":
        theme_button_text = "🌓 Auto"
        help_text = "Currently: Auto (follows browser). Click → Light mode."
    elif current_mode == "light":
        theme_button_text = "☀️ Light"
        help_text = "Currently: Light mode. Click → Dark mode."
    else:
        theme_button_text = "🌙 Dark"
        help_text = "Currently: Dark mode. Click → Auto mode."

    if st.button(theme_button_text, help=help_text, key="theme_toggle"):
        if current_mode == "auto":
            st.session_state.theme_mode = "light"
        elif current_mode == "light":
            st.session_state.theme_mode = "dark"
        else:
            st.session_state.theme_mode = "auto"
        st.rerun()


# MLPerf version configuration
mlperf_versions = {
    "v5.1": "mlperf-data/mlperf-5.1.csv",
    "v5.0": "mlperf-data/mlperf-5.0.csv",
}

# Render the MLPerf dashboard
render_mlperf_dashboard(mlperf_versions)

