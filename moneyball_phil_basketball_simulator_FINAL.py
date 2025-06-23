# Streamlit Basketball App - Complete Template

import streamlit as st
from PIL import Image

# Load assets
logo_image = Image.open("moneyball_logo.png")
background_image = Image.open("basketball_court_background.png")

# App Layout
st.set_page_config(layout="centered")
st.image(logo_image, width=250)
st.markdown("<h1 style='text-align: center;'>MoneyBall Phil: Basketball Simulator</h1>", unsafe_allow_html=True)
st.image(background_image, use_column_width=True)

# Player Stat Inputs
with st.form("player_input"):
    st.subheader("🧾 Player Stats Entry")
    name = st.text_input("Player Name")
    pts = st.number_input("Points", value=0)
    reb = st.number_input("Rebounds", value=0)
    ast = st.number_input("Assists", value=0)
    usage = st.slider("Usage Rate (%)", 0.0, 100.0, 20.0)
    era = st.number_input("Opponent ERA (if available)", value=0.0)
    odds = st.text_input("Sportsbook Odds (e.g. -120)")
    submitted = st.form_submit_button("Simulate Player")

# Placeholder for calculation and board
if submitted:
    st.success(f"Simulated {name}'s performance and evaluated against PRA/Points target.")
    st.write(f"**Stats:** {pts} PTS, {reb} REB, {ast} AST | **Usage:** {usage}% | **Odds:** {odds}")
    st.write("📊 PRA = ", pts + reb + ast)

# Add-on placeholders
st.markdown("### 🔥 Top Player Board")
st.dataframe({"Player": [name], "PRA": [pts + reb + ast], "Usage": [f"{usage}%"], "Odds": [odds]})

st.markdown("### 🧮 Parlay Evaluator (Coming Soon)")

