import streamlit as st
from datetime import date, datetime
import os

# Streamlit page config
st.set_page_config(page_title="Rafeed Tracker", page_icon="💬", layout="centered")

PASSWORD = "fablab511"  # Change this to a password only you & your friend know

password = st.sidebar.text_input("Enter password to access", type="password")

if password != PASSWORD:
    st.warning("⚠️ Please enter the correct password to continue.")
    st.stop()

# File to store last texted date
DATA_FILE = "last_texted.txt"
DEFAULT_DATE = date(2025, 6, 3)

# Load last_texted date
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        try:
            last_texted = datetime.strptime(f.read().strip(), "%Y-%m-%d").date()
        except:
            last_texted = DEFAULT_DATE
else:
    last_texted = DEFAULT_DATE
    with open(DATA_FILE, "w") as f:
        f.write(str(DEFAULT_DATE))

today = date.today()
days_since = (today - last_texted).days

# Mood avatar
if days_since == 0:
    avatar = "😊"
elif days_since == 1:
    avatar = "😐"
elif 2 <= days_since <= 3:
    avatar = "😕"
elif 4 <= days_since <= 5:
    avatar = "😟"
else:
    avatar = "😢"

# Custom CSS styling
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .main > div {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 25px;
        padding: 40px 60px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
        max-width: 600px;
        margin: 50px auto;
    }
    .counter-box {
        display: flex;
        align-items: center;
        justify-content: center;
        background: #48cae4;
        border-radius: 30px;
        padding: 40px 60px;
        box-shadow: 0 12px 30px rgba(72, 202, 228, 0.5);
        margin-top: 0;
        margin-bottom: 30px;
        color: white;
    }
    .calendar-icon {
        font-size: 100px;
        margin-right: 30px;
        filter: drop-shadow(1px 1px 1px rgba(0,0,0,0.2));
    }
    .days-number {
        font-size: 110px;
        font-weight: 900;
        color: #03045e;
        text-shadow: 1px 1px 4px rgba(255,255,255,0.7);
    }
    .last-texted {
        font-size: 26px;
        font-weight: 700;
        text-align: center;
        color: #023e8a;
        margin-bottom: 30px;
        letter-spacing: 1.1px;
    }
    div[style*="font-size: 80px;"] {
        font-size: 140px !important;
        margin-bottom: 40px;
        text-align: center !important;
        filter: drop-shadow(1px 1px 2px rgba(0,0,0,0.15));
        user-select: none;
    }
    .emoji-container {
        display: flex;
        justify-content: center;
        gap: 100px;
        flex-wrap: wrap;
        margin-top: 20px;
    }
    .emoji-wrapper {
        position: relative;
        display: inline-block;
        text-align: center;
        cursor: pointer;
        user-select: none;
        transition: transform 0.3s ease;
    }
    .emoji-wrapper:hover {
        transform: scale(1.3);
        filter: drop-shadow(0 5px 8px rgba(0, 0, 0, 0.15));
    }
    button.stButton > button {
        font-size: 110px !important;
        background: none !important;
        border: none !important;
        padding: 0 !important;
        margin: 0 !important;
        cursor: pointer !important;
        transition: transform 0.3s ease !important;
    }
    button.stButton > button:hover {
        transform: scale(1.3) !important;
    }
    .tooltip {
        visibility: hidden;
        background-color: #023e8a;
        color: #fff;
        text-align: center;
        border-radius: 8px;
        padding: 7px 14px;
        position: absolute;
        bottom: 125%;
        left: 50%;
        transform: translateX(-50%);
        white-space: nowrap;
        opacity: 0;
        transition: opacity 0.4s ease;
        font-size: 17px;
        font-weight: 600;
        letter-spacing: 0.5px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.3);
        user-select: none;
    }
    .emoji-wrapper:hover .tooltip {
        visibility: visible;
        opacity: 1;
    }
    .slap-text {
        font-size: 26px;
        font-weight: 700;
        text-align: center;
        margin-top: 20px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #d90429;
        user-select: none;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
    }
    .eid-card {
        position: fixed;
        top: 20px;
        left: 20px;
        background: #90caf9;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.25);
        width: 240px;
        user-select: none;
        font-weight: 800;
        color: #0d47a1;
        cursor: pointer;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        transition: background 0.3s ease;
        z-index: 9999;
    }
    .eid-card:hover {
        background: #64b5f6;
    }
    .eid-card summary {
        list-style: none;
        padding: 12px 20px;
        font-size: 20px;
        border-radius: 15px;
        outline: none;
        display: block;
        white-space: nowrap;
        user-select: none;
    }
    .eid-card[open] {
        width: 280px;
    }
    .eid-content {
        padding: 15px 20px 25px 20px;
        font-size: 20px;
        color: #0d47a1;
        border-top: 2px solid #0d47a1;
        user-select: text;
        text-align: center;
    }
    .eid-card summary::-webkit-details-marker {
        display: none;
    }
    .eid-card summary::marker {
        content: "";
    }
    </style>
""", unsafe_allow_html=True)

# Eid card
st.markdown("""
<details class="eid-card" role="region" aria-label="Eid Mubarak Card">
  <summary>EID MUBARAK 🎉</summary>
  <div class="eid-content">EID MUBARAK FABLIHA! 🌙🐮</div>
</details>
""", unsafe_allow_html=True)

# Mood display
st.markdown(f"""
<div class="counter-box">
    <div class="calendar-icon">📅</div>
    <div class="days-number">{days_since}</div>
</div>
<div class="last-texted">Last texted on: {last_texted.strftime('%B %d, %Y')}</div>
<div style="font-size: 80px; text-align: center;">{avatar}</div>
""", unsafe_allow_html=True)

# Control flags
show_cheers = False
show_slap = False
show_reset = False

# Emoji buttons
st.markdown('<div class="emoji-container">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="emoji-wrapper"><div class="tooltip">I will text</div>', unsafe_allow_html=True)
    if st.button("🐶", key="she_texted", help="I will text", use_container_width=True):
        with open(DATA_FILE, "w") as f:
            f.write(str(today))
        show_cheers = True
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="emoji-wrapper"><div class="tooltip">Slap Rafeed!</div>', unsafe_allow_html=True)
    if st.button("🐧", key="slap", help="Slap Rafeed!", use_container_width=True):
        show_slap = True
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="emoji-wrapper"><div class="tooltip">Reset to June 3</div>', unsafe_allow_html=True)
    if st.button("😾", key="reset", help="Back to square one", use_container_width=True):
        with open(DATA_FILE, "w") as f:
            f.write(str(DEFAULT_DATE))
        show_reset = True
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close emoji-container

# Display feedback
if show_cheers:
    if os.path.exists("cheers.gif"):
        with open("cheers.gif", "rb") as f:
            gif_bytes = f.read()
        st.image(gif_bytes, use_container_width=True)
        st.markdown('<div class="slap-text" style="color: #40916c;">Rafeed is smiling again 😊</div>', unsafe_allow_html=True)
    else:
        st.error("cheers.gif not found.")

if show_slap:
    if os.path.exists("slap.gif"):
        with open("slap.gif", "rb") as f:
            gif_bytes = f.read()
        st.image(gif_bytes, use_container_width=True)
        st.markdown('<div class="slap-text">That\'s what you get Rafeed for misbehaving!😠</div>', unsafe_allow_html=True)
    else:
        st.error("slap.gif not found.")

if show_reset:
    if os.path.exists("cry.gif"):
        with open("cry.gif", "rb") as f:
            gif_bytes = f.read()
        st.image(gif_bytes, use_container_width=True)
    else:
        st.error("cry.gif not found.")
    
    st.markdown(
        '<div class="slap-text" style="color: #e76f51;">No I still won\'t text. Keep counting! 😑</div>',
        unsafe_allow_html=True
    )


