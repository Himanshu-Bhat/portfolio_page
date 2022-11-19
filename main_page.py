# Required Libraries
import streamlit as st
from streamlit_option_menu import option_menu
from pathlib import Path
import requests
from streamlit_lottie import st_lottie
from PIL import Image

# ---- Page Config ----
# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Himanshu Bhat", page_icon=":globe_with_meridians:", layout="wide")


# ---- PATH SETTINGS ----
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
home_css_file = current_dir / "styles" / "home_page.css"
contact_css_file = current_dir / "styles" / "content_page.css"
profile_image = current_dir / "images" / "profile_pic.png"
profile_picture = Image.open(profile_image)
# resume_file = current_dir / "assets" / "CV.pdf"


# ---- LottieFile Function ----
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# ---- Horizontal Menu / NavBar with custom style ----
selected = option_menu(
    menu_title=None,  # required
    options=["HOME", "PROJECTS", "CONTACT"],  # required
    icons=["bi-person-circle", "bi-code-slash", "bi bi-chat-left-dots-fill"],  # optional
    menu_icon="cast",  # BootStrap Icon: https://icons.getbootstrap.com/
    default_index=0,  # optional
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#080808"},
        "icon": {"color": "white", "font-size": "20px"},
        "nav-link": {"font-size": "20px",
                     "text-align": "right",
                     "margin": "0px",
                     "--hover-color": "#080808"},
        "nav-link-selected": {"background-color": "080808"},
    },
)


# ------------------------------------- Home Page Content -----------------------------------------------
def home_page():
    for i in range(1):
        st.write('\n')
    ###################################### BLOCK-1 #######################################################
    # ---- FRONT PAGE ----
    col1, col2, col3, col4 = st.columns([1, 4, 4, 1], gap='medium')

    with col2:  # Profile Photo
        st.image(profile_picture, width=300)

    with col3:  # Introduction
        name = "Himanshu Bhat"
        text_style = f"<h1 style='font-family:Georgia, serif; color:#f8f8ff; font-size:55px;'>{name}</h1>"
        st.markdown(text_style, unsafe_allow_html=True)

        intro_content = """Software Engineer at DXC Technology"""
        text_style = f"<p1 style='font-family:serif; color:grey; font-size:26px;'>{intro_content}</p1>"
        st.markdown(text_style, unsafe_allow_html=True)

        text = """3+ Years of Experience In Assisting Enterprises & Business By Supporting <br> Application Management & Private Cloud Solutions."""
        text_style = f"<p1 style='font-family:san-system-ui; color:#f9ffe3; font-size:16px;'>{text}</p1>"
        st.markdown(text_style, unsafe_allow_html=True)

    ###################################### BLOCK-2 #######################################################
    # --- EXPERIENCE & QUALIFICATIONS ---
    for i in range(3):
        st.write('\n')

    col1, col2, col3, col4 = st.columns([1, 5, 3, 1], gap='medium')

    with col2:
        heading = "Experience & Qualifications"
        string = f"<h1 style='font-family:sans-serif; color:#7B68EE; font-size:25px;'>{heading}</h1>"
        st.markdown(string, unsafe_allow_html=True)

        st.write("""
                 - ✔️ 3+ Years experience in IT Industry, Working on across multiple Technologies and Project.
                 - ✔️ Strong hands on experience and knowledge in Python. 
                 - ✔️ Good understanding of statistical principles and their respective applications.
                 - ✔️ ️ Excellent team-player and displaying strong sense of initiative on tasks.
                """)

    with col3:
        lottie_url = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_qp1q7mct.json")
        st_lottie(
            lottie_url,
            speed=1,
            reverse=False,
            loop=True,
            quality="low",  # medium ; high
            height=200,
            width=300,
            key=None,
        )

    ###################################### BLOCK-3 #######################################################
    # ---- SKILLS ----
    for i in range(3):
        st.write('\n')

    col1, col2, col3, col4 = st.columns([1, 3.5, 4.5, 1], gap='small')

    with col2:
        lottie_url = load_lottieurl("https://assets8.lottiefiles.com/private_files/lf30_8z6ubjgk.json")
        st_lottie(
            lottie_url,
            speed=3,
            reverse=False,
            loop=True,
            quality="low",  # medium ; high
            height=400,
            width=400,
            key=None,
        )

    with col3:
        for i in range(1):
            st.write(' ')

        heading = "Skills"
        string = f"<h1 style='font-family:sans-serif; color:#2ecc71; font-size:25px;'>{heading}</h1>"
        st.markdown(string, unsafe_allow_html=True)

        st.write("""
            - 👩‍💻 Programming : Python, SQL, Mainframe, JCL, REXX
            
            - 📊 Data Analysis & Visualization : Tableau, Spreadsheets, Pandas, Matplotlib, Seaborn
            
            - 📚 Modeling : Machine Learning, Natural Language Processing (nltk), PySpark (MLlib)
            
            - 🗄️ Familiar With : Cloud, Git, MongoDB, Docker
                 """)

    ###################################### BLOCK-4 #######################################################
    # ---- EXPERIENCE ----
    st.write('\n')

    col1, col2, col3, col4 = st.columns([1, 5, 3.5, .5], gap='medium')

    with col2:
        heading = "Work Experience"
        string = f"<h1 style='font-family:sans-serif; color:#4f86f7; font-size:25px;'>{heading}</h1>"
        st.markdown(string, unsafe_allow_html=True)

        # --- JOB 1 ---
        st.write("🏢", "**DXC Technology**  | *11/2022 - Present*")
        st.write("""
                - ► To be filled
                """)

        # --- JOB 2 ---
        st.write("🏢", "**Kyndryl**  | *09/2021 - 10/2022*")
        st.write("""
                - ► Automated Database processing, Increased efficiency by 30%
                - ► Designed and Implemented SOP for Automated System Management, reducing 0.10 FTE
                - ► Build SharePoint tool for global team
                """)

        # --- JOB 3 ---
        st.write("🏢", "**IBM**  | *01/2020 - 08/2021*")
        st.write("""
                - ► Developed scripts for migration from CA Reporting Tool, Saving incremental license cost of $25000  
                - ► Handled ad-hoc requests including management issues in a timely and efficient manner
                - ► Automated manual process using scripts, Increased the efficiency by 50%
                """)

        # --- JOB 4 ---
        st.write("🏢", "**CRISPS**  | *Internship*")
        st.write("""
                - ► Engineered a NLP model using GPT2 and XLNet for preparing a summary of long paragraphs
                - ► Automated a manual imaging processing procedure through a python script saving manual time.
                """)

    with col3:
        st.write(' ')
        lottie_url = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_cmaqoazd.json")
        st_lottie(
            lottie_url,
            speed=1,
            reverse=False,
            loop=True,
            quality="low",  # medium ; high
            height=350,
            width=350,
            key=None,
        )

    ###################################### BLOCK-5 #######################################################
    # ---- CERTIFICATION ----
    st.write('\n')

    col1, col2, col3, col4 = st.columns([1, 4, 4, 1], gap='medium')

    with col2:
        lottie_url = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_tbwqrxnz.json")
        st_lottie(
            lottie_url,
            speed=1,
            reverse=False,
            loop=True,
            quality="low",  # medium ; high
            height=350,
            width=350,
            key=None,
        )

    with col3:
        for i in range(3):
            st.write(' ')

        heading = "Certifications"
        string = f"<h1 style='font-family:sans-serif; color:#efcc00; font-size:25px;'>{heading}</h1>"
        st.markdown(string, unsafe_allow_html=True)

        certficates = {
            "Google Data Analytics Professional Certificate": "https://www.credly.com/badges/38a9c22b-eeae-4298-b637-80a7c94353af/linked_in_profile",
            "IBM Python for Data Science": "https://www.credly.com/badges/f3fbbb15-1694-45b6-9ee7-48e90d5b0591?source=linked_in_profile",
            "IBM Data Science Foundations - Level 2": "https://www.credly.com/badges/88cfb4da-c2b1-4571-9383-7c97f2679617?source=linked_in_profile",
            "Machine Learning with Python": "https://www.credly.com/badges/7d5a605c-0757-44e1-b059-bd8c0b8e7430/public_url",
            "Microsoft Certified Azure Fundamental AZ-900": "https://www.credly.com/badges/c72463eb-67b0-4f2c-9962-4335b3f52641?source=linked_in_profile",
        }
        for certficate, link in certficates.items():
            st.write(f"[🏆 {certficate}]({link})")

    # Use Local Contact CSS File
    with open(home_css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# ------------------------------------- Contact Page Content -----------------------------------------------
def contact_page():
    col1, col2 = st.columns([2.2, 4], gap='large')
    with col1:
        heading = "🤳 You Can Connect With Me On :"
        string = f"<h1 style='font-family:sans-serif; color:#00b7eb; font-size:30px;'>{heading}</h1>"
        st.markdown(string, unsafe_allow_html=True)
        st.write('')
        # Email Id
        heading = """
                  Email id : himanshu.bhat007@gmail.com
                  """
        string = f"<p1 style='font-family:sans-serif; color:#efcc00; font-size:18px;'>{heading}</p1>"
        st.markdown(string, unsafe_allow_html=True)
        # LinkedIn
        heading = "LinkedIn : linkedin.com/in/himanshu-bhat/in"
        string = f"<p1 style='font-family:sans-serif; color:#efcc00; font-size:18px;'>{heading}</p1>"
        st.markdown(string, unsafe_allow_html=True)

    with col2:  # Contact Me LottiFile
        lottie_url = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_u25cckyh.json")
        st_lottie(lottie_url,
                  speed=.5,
                  reverse=False,
                  loop=True,
                  quality="low",  # medium ; high
                  height=200,
                  width=200,
                  key=None
                  )

    col1, col2 = st.columns([2.2, 4], gap='large')

    with col1:
        heading = "📬 Or Leave Me a Message!"
        string = f"<h1 style='font-family:sans-serif; color:#1e90ff; font-size:30px;'>{heading}</h1>"
        st.markdown(string, unsafe_allow_html=True)

    contact_form = """
                    <form action="https://formsubmit.co/himanshu.bhat008@gmail.com" method="POST">
                    <input type="hidden" name="_captcha" value="true">
                    <input type="text" name="name" placeholder="Your name" required>
                    <input type="email" name="email" placeholder="Your email" required>
                    <textarea name="message" placeholder="Your message here"></textarea>
                    <button type="submit">Send</button>
            </form>"""

    st.markdown(contact_form, unsafe_allow_html=True)

    # Use Local Contact CSS File
    with open(contact_css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# ---- NavBar ----
if selected == "HOME":
    home_page()
elif selected == "PROJECTS":
    pass
else:
    contact_page()

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
