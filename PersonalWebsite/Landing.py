import streamlit as st
import info
import base64

def show_rounded_image(image_path, width=None, border_radius=20):
    """
    Display an image in Streamlit with rounded corners at full quality.

    Args:
        image_path (str): Path to the image file.
        width (int, optional): Display width in pixels. Keeps aspect ratio.
        border_radius (int, optional): Radius for rounded corners in pixels.
    """
    with open(image_path, "rb") as f:
        img_bytes = f.read()
    b64 = base64.b64encode(img_bytes).decode()
    width_attr = f' width="{width}"' if width else ""
    st.markdown(
        f'<img src="data:image/jpeg;base64,{b64}"{width_attr} style="border-radius:{border_radius}px;">',
        unsafe_allow_html=True
    )

show_rounded_image("PersonalWebsite/Images/profile.jpg", width=200, border_radius=100)

st.write("")
st.subheader("Harini Penumuchu")
st.write("Hi! I’m Harini, a student at Georgia Tech. My interests broadly span hardware design, computer architecture and machine learning. Recently, I’ve worked on projects in computational physics and applications for visualizing large-scale datasets. Growing up in the San Francisco Bay Area taught me to always be excited about technology, so please don’t hesitate to reach out with any exciting ideas or opportunities!")
st.write("hpenumuchu3 [at] gatech [dot] edu")
def links_section():
    st.sidebar.header("💌 Links")
    linkedin_link = f'<a href="{info.my_linkedin_url}"><img src="{info.linkedin_image_url}" alt="LinkedIn" width = "40" height = "40"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
    github_link = f'<a href="{info.my_github_url}"><img src="{info.github_image_url}" alt="Github" width = "40" height = "40"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)
    email_html = f'<a href = "mailto:{info.my_email_address}"><img src="{info.email_image_url}" alt = "Email" width = "40" height = "40"></a>'
    st.sidebar.markdown(email_html, unsafe_allow_html = True)

links_section()
