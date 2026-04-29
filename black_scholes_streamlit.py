import streamlit as st
from black_scholes_formula import black_scholes
from black_scholes_visualization import visualize_black_scholes, calculate_data

st.set_page_config(layout="wide")
#Sidebar
st.sidebar.title("Black-Scholes Model")
st.sidebar.number_input(
    label="Current Asset Price",
    min_value=0.00,
    value=100.00,
    step=1.00,
    key="S"
)
st.sidebar.number_input(
    label="Strike Price",
    min_value=0.00,
    value=100.00,
    step=1.00,
    key="K"
)
st.sidebar.number_input(
    label="Time to Maturity (Years)",
    min_value=0.00,
    value=1.00,
    step=0.05,
    key="T"
)
st.sidebar.number_input(
    label="Volatility",
    min_value=0.00,
    max_value=1.00,
    value=0.20,
    step=0.01,
    key="V"
)
st.sidebar.number_input(
    label="Risk-Free Interest Rate",
    min_value=0.00,
    max_value=1.00,
    value=0.02,
    step=0.01,
    key="r"
)
st.sidebar.divider()
st.sidebar.button("Heatmap Parameters")
st.sidebar.number_input(
    label="Min Spot Price",
    min_value=0.00,
    value=80.00,
    step=1.00,
    key="S_min"
)
st.sidebar.number_input(
    label="Max Spot Price",
    min_value=0.00,
    value=120.00,
    step=1.00,
    key="S_max"
)
st.sidebar.slider(
    label="Min Volatility for Heatmap",
    min_value=0.00,
    max_value=1.00,
    value=0.10,
    step=0.01,
    key="V_min"
)
st.sidebar.slider(
    label="Max Volatility for Heatmap",
    min_value=0.00,
    max_value=1.00,
    value=0.30,
    step=0.01,
    key="V_max"
)

# Main Site
st.title("Black-Scholes Pricing Model")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Current Asset Price", round(st.session_state["S"], 2))
col2.metric("Strike Price", round(st.session_state["K"], 2))
col3.metric("Time to Maturity (Years)", round(st.session_state["T"], 2))
col4.metric("Volatility", round(st.session_state["V"], 2))

col5.metric("Risk-Free Interest Rate", round(st.session_state["r"], 2))
call, put = black_scholes(st.session_state["r"], 
                          st.session_state["S"],
                          st.session_state["T"],
                          st.session_state["V"],
                          st.session_state["K"])

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
        <div style="background-color: #eb9973; padding: 20px; border-radius: 10px; text-align: center;">
            <p>CALL Value</p>
            <h2>${call:.2f}</h2>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div style="background-color: #602969; padding: 20px; border-radius: 10px; text-align: center;">
            <p>PUT Value</p>
            <h2>${put:.2f}</h2>
        </div>
    """, unsafe_allow_html=True)

st.divider()
st.title("Options Price - Heatmap")
fig1, fig2 = visualize_black_scholes(*calculate_data(
    st.session_state["r"],
    st.session_state["S_min"],
    st.session_state["S_max"],
    st.session_state["T"],
    st.session_state["V_min"],
    st.session_state["V_max"],
    st.session_state["K"],
))

col1, col2 = st.columns(2)

with col1:
    st.pyplot(fig1)

with col2:
    st.pyplot(fig2)