import streamlit as st
import info
import pandas as pd

#Sidebar Links
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

st.link_button("Printable Resume", "https://www.dropbox.com/scl/fi/d1tpxocwbkyubwt4bp7mc/Spring-2026-Resume.pdf?rlkey=ht28yrjc59rsj0dwq7vph3i9j&st=hav2usai&dl=0")

st.divider()
#Education
def education_section():
    st.markdown('<p style="font-size:20px;font-weight:bold;">📖 Education</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:20px;font-weight:bold;">Georgia Institute of Technology</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:16px;font-style: italic;">Electrical Engineering / Minor in Computer Science</p>', unsafe_allow_html=True)
    st.markdown(
    ":green-badge[:material/star_shine: GPA 4.00]")
            
        
    st.markdown("**Relevant Coursework:**")

    st.markdown(
        ":violet-badge[Object-Oriented Programming] "
        ":violet-badge[Digital System Design] "
        ":violet-badge[Linear Algebra] "
    )

    st.markdown(
        ":violet-badge[Physics II] "
        ":violet-badge[Differential Equations] "
        ":violet-badge[Intro to Computing] "
    )
        
    st.markdown('<p style="font-size:20px;font-weight:bold;">Foothill High School</p>', unsafe_allow_html=True)
    st.markdown(
    ":green-badge[:material/star_shine: GPA 4.45]")
    st.markdown(
    ":blue-badge[:material/school: National Merit Finalist]")
    st.divider()

education_section()


#Professional Experience

def experience_section():
    st.markdown('<p style="font-size:20px;font-weight:bold;">🖥️ Experience</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:20px;font-weight:bold;">Yellow Jacket Space Program (YJSP)</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:16px;font-style: italic;font-weight:bold;">Avionics Engineer | Hardware-in-the-Loop (HITL)</p>', unsafe_allow_html=True)
    st.write("• Designed a PCB to test Yellow Jacket Space Program thermocouple sensors, incorporating ESD, over/undervoltage, and reverse-polarity protection, filtering, and voltage regulation")
    st.write("• Integrated an STM32 MCU with JTAG and SPI to interface with an ADC")
    st.write("• Developing schematics for YJSP’s Hardware-in-the-Loop (HITL) project to enable full hardware verification under normally impossible testing conditions")
    st.write("• Redesigning YJSP’s Ground System Avionics Module (Ground SAM) to improve reliability, testability, and system integration")
    st.write("")
    st.markdown('<p style="font-size:20px;font-weight:bold;">Facility for Rare Isotope Beams</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:16px;font-style: italic;font-weight:bold;">Intern | Computational Physics</p>', unsafe_allow_html=True)
    st.write("• Built an interactive GUI for parsing large-scale ROOT datasets and visualizing neutron scattering behavior")
    st.write("• Implemented real-time data processing and dynamic visualizations to support beamline experiments")
    st.write("• Presented research at American Physical Society (APS) Conference; tool has since been actively used in multiple experiments")

    st.divider()
    
experience_section()

def recognition_section():
    st.markdown('<p style="font-size:20px;font-weight:bold;">🫀 Recognition</p>', unsafe_allow_html=True)
    st.markdown(
    ":blue-badge[:material/star_shine: National Merit Finalist (2025)]")
    st.markdown(
    ":blue-badge[:material/star_shine: We the People CA State Champion and National Finalist (2025)]")
    st.markdown(
    ":blue-badge[:material/star_shine: Berkeley Math Tournament Top 20 Percent in Algebra/Discrete (2024)]")
    st.markdown(
    ":blue-badge[:material/star_shine: Rise Global Finalist (2024)]")
    st.markdown(
    ":blue-badge[:material/star_shine: 2x American Invitational Mathematics Exam (AIME) Qualifier (2024)]")

recognition_section()
    
    



