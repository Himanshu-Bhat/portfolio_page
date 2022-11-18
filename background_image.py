import base64
import streamlit as st


with open("Background.jpg", "rb") as f:
    data = f.read()
img = base64.b64encode(data).decode()


page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://wallpaperaccess.com/full/46542.jpg");
background-size: 100%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
