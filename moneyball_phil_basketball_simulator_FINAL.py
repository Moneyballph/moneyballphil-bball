
import streamlit as st
from PIL import Image
import os

st.set_page_config(layout="wide")

# Load background and logo
background_image = "assets/basketball_court_background.png"
logo_image = "assets/moneyball_phil_basketball_logo.png"

# Custom background style
st.markdown(f'''
    <style>
        .stApp {{
            background-image: url("{{background_image}}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .custom-title {{
            font-size: 3em;
            color: white;
            font-weight: bold;
            text-align: center;
            margin-top: 1rem;
        }}
    </style>
''', unsafe_allow_html=True)

# Display logo and title
st.image(logo_image, width=250)
st.markdown('<div class="custom-title">MoneyBall Phil: NBA Simulator</div>', unsafe_allow_html=True)

# Placeholder for further app development
st.markdown("### Coming Soon: Full PRA + Points Player Simulator")
