import streamlit as st
from PIL import Image
import os

# Load assets
logo_path = "assets/moneyball_phil_logo.png"
background_path = "assets/basketball_arena_background.png"

# Page config
st.set_page_config(page_title="MoneyBall Phil - Basketball", layout="wide")

# Custom CSS for background
st.markdown(f'''
    <style>
    .stApp {{
        background-image: url("https://raw.githubusercontent.com/yourusername/moneyball_phil_basketball_app/main/assets/basketball_arena_background.png");
        background-size: cover;
        background-position: center;
    }}
    </style>
''', unsafe_allow_html=True)

# Load and display logo
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image(logo_path, width=300)

# App header
st.markdown("## 🏀 MoneyBall Phil - NBA Simulator")
st.markdown("Simulate player props. Track elite plays. Dominate your sportsbook.")
