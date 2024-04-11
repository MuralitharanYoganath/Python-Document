from pathlib import Path

import streamlit as st 
from PIL import Image



# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "styles" / "Muralitharan.pdf"
profile_pic = current_dir / "styles" / "MT.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Muralitharan Yoganath"
PAGE_ICON = ":wave:"
NAME = "Muralitharan Yoganath"
DESCRIPTION = """
A fresher Java full stack developer in some new the learning to working the Java Programming language for tasks suh as web development(Html,Css,Javascript),DataBase(Sql),J2EE(JDBC,Servlet)
There are teams writing code structure to design on provide a project 
There are also beginning to underrstand the importance of testing or Developers and Documentation for ensuring code provide Quality 
"""
EMAIL = "muraliemailz@email.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/muralitharan-yoganath-124085293/",
    "GitHub": "https://github.com/MuralitharanYoganath",
}
PROJECTS = {
    "🏆VANET BASED PRIVACY PRESERVING COMMUNICATION SCHEME(Domain:Network) Main project:" "https://github.com/MuralitharanYoganath/My-Project",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

col1, col2  = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=250)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

    # --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE ---
st.write('\n')
st.subheader("**EXPERIENCE CERTIFICATE & INTERNSHIP**")
st.write("""
- **Imagecon Internship**
    - ✔️Cloud music Project
- **Paper Presentation**
    - ✔️KIOT National Level
    - ✔️Kavery Natioal Level
"""
)