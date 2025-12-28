import streamlit as st
import info
import pandas as pd

def links_section():
    st.sidebar.header("💌 Links")
    linkedin_link = f'<a href="{info.my_linkedin_url}"><img src="{info.linkedin_image_url}" alt="LinkedIn" width = "30" height = "30"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
    github_link = f'<a href="{info.my_github_url}"><img src="{info.github_image_url}" alt="Github" width = "30" height = "30"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)
    email_html = f'<a href = "mailto:{info.my_email_address}"><img src="{info.email_image_url}" alt = "Email" width = "30" height = "30"></a>'
    st.sidebar.markdown(email_html, unsafe_allow_html = True)

links_section()


def dual_text(left_text, right_text, left_style="", right_style=""):
    """
    Display two pieces of text on the same line: left-aligned and right-aligned.
    
    Args:
        left_text (str): Text to align left.
        right_text (str): Text to align right.
        left_style (str): Optional CSS for left text (e.g., "font-size:20px; color:red;").
        right_style (str): Optional CSS for right text.
    """
    st.markdown(
        f"""
        <div style="display: flex; justify-content: space-between;">
            <span style="{left_style}">{left_text}</span>
            <span style="{right_style}">{right_text}</span>
        </div>
        """,
        unsafe_allow_html=True
    )

def projects():
    dual_text(
    "BART Web App",
    "2025",
    left_style="font-size:20px; font-weight:bold;",
    right_style="font-size:16px;")
    st.write("")
    st.write("Built a multi-page web app that processes real-time BART API data and generates system summaries using Google Gemini LLM")
    st.link_button("link <3", "https://bartdata.streamlit.app/")


    

    
projects()
