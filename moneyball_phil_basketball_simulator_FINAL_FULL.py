
import streamlit as st
from PIL import Image
import math

# Set page config
st.set_page_config(layout="wide")

# Load and display background
background_image = "basketball_arena_bg.png"
logo_image = "moneyball_basketball_logo.png"

# Apply full-screen background via CSS
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background: url('{background_image}');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}
[data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Display logo in top-left
st.image(logo_image, width=180)

st.title("🏀 Moneyball Phil: Basketball Simulator")

st.markdown("Simulate player PRA or Points probability based on advanced usage stats.")

# Select stat type
stat_type = st.selectbox("📊 What stat do you want to simulate?", ["PRA", "Points"])

with st.form("player_stats"):
    col1, col2 = st.columns(2)
    with col1:
        player_name = st.text_input("Player Name")
        points = st.number_input("Points Per Game", min_value=0.0, step=0.1)
        rebounds = st.number_input("Rebounds Per Game", min_value=0.0, step=0.1)
        assists = st.number_input("Assists Per Game", min_value=0.0, step=0.1)
        usage_rate = st.number_input("Usage Rate %", min_value=0.0, max_value=100.0, step=0.1)

    with col2:
        opponent = st.text_input("Opponent Team")
        position = st.selectbox("Player Position", ["PG", "SG", "SF", "PF", "C"])
        line_value = st.number_input(f"{stat_type} Line", min_value=0.0, step=0.5)
        over_odds = st.number_input("Over Odds (American)", value=-110)
        under_odds = st.number_input("Under Odds (American)", value=-110)

    submitted = st.form_submit_button("Simulate Player")

# Utility functions
def american_to_prob(odds):
    if odds < 0:
        return abs(odds) / (abs(odds) + 100)
    else:
        return 100 / (odds + 100)

def simulate_hit_probability(avg, line, variance=0.15):
    z = (line - avg) / (variance * avg if avg > 0 else 1)
    return 1 / (1 + math.exp(z))

def get_hit_zone(prob):
    if prob >= 0.80:
        return "🔥 Elite"
    elif prob >= 0.70:
        return "💪 Strong"
    elif prob >= 0.60:
        return "🟡 Moderate"
    else:
        return "🔻 Below Average"

if submitted:
    if stat_type == "PRA":
        avg = points + rebounds + assists
    else:
        avg = points

    true_prob = simulate_hit_probability(avg, line_value)
    implied_over = american_to_prob(over_odds)
    implied_under = american_to_prob(under_odds)
    ev_over = round((true_prob - implied_over) * 100, 1)
    ev_under = round(((1 - true_prob) - implied_under) * 100, 1)

    st.markdown(f"### 🎯 Results for **{player_name}** vs **{opponent}**")
    st.markdown(f"- **Stat Type:** {stat_type}")
    st.markdown(f"- **Line:** {line_value}")
    st.markdown(f"- **Simulated True Probability (Over):** `{true_prob:.2%}`")
    st.markdown(f"- **Over EV:** `{ev_over:.1f}%`")
    st.markdown(f"- **Under EV:** `{ev_under:.1f}%`")
    st.markdown(f"- **Hit Zone:** `{get_hit_zone(true_prob)}`")
