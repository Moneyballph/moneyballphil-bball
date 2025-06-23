
import streamlit as st
from PIL import Image

# Load assets
logo = Image.open("ChatGPT Image Jun 22, 2025, 05_53_13 PM.png")
background = Image.open("ChatGPT Image Jun 22, 2025, 05_45_45 PM.png")

# Set page config
st.set_page_config(layout="wide")

# Display background
st.image(background, use_column_width=True)

# Overlay logo
st.image(logo, width=200)

st.title("MoneyBall Phil: Basketball Simulator")

# Placeholder for future features
st.markdown("Coming soon: Player Inputs, PRA/Points Simulation, Parlay Builder, and Top Player Board.")
