import streamlit as st

# Set page config
st.set_page_config(page_title="Professional Portfolio", layout="wide")

# --- HEADER SECTION ---
col1, col2 = st.columns([1, 3], gap="small")
with col1:
    st.image("https://via.placeholder.com/150")  # Replace with your professional photo URL

with col2:
    st.title("Analytical Chemist & Data Enthusiast")
    st.write("Specializing in Quality Assurance, Laboratory Standards, and Technical Oversight.")
    st.write("📍 Kenya | [LinkedIn](#) | [GitHub](#)")

# --- TECHNICAL AUTHORITY ---
st.write("---")
st.subheader("Technical Expertise & Standards")
st.write("""
- **International Standards:** ISO 17025, ISO 19011, GAMP 5.
- **Programming:** Python (Logic, Data Handling, Automation).
- **Core Competencies:** Quality Assurance, Operational Oversight, Technical Auditing.
""")

# --- PROJECTS & TOOLS ---
st.write("---")
st.subheader("Technical Projects")
col_a, col_b = st.columns(2)

with col_a:
    st.write("**Python Automation Tools**")
    st.write("- Developed custom scripts for temperature conversion and grading logic.")
    st.write("- Built a multi-user login validator with secure error handling.")

with col_b:
    st.write("**Operational Expertise**")
    st.write("- Oversight of technical water systems (Resin regeneration & RO membrane systems).")
    st.write("- Implementation of QA protocols in pharmaceutical manufacturing.")

# --- FOOTER ---
st.write("---")
st.download_button(label="📄 Download Standard CV", data="Your CV Content", file_name="CV.pdf")
