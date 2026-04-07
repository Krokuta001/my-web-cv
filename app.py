import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="John Muya Kariuki | Professional Portfolio", layout="wide")

# 2. Header / Hero Section
col1, col2 = st.columns([3, 1])
with col1:
    st.title("John Muya Kariuki")
    st.subheader("Validation Officer & Analytical Chemist")
    st.write("📍 Kenya | 📧 jmuya47@hotmail.com | 📞 +254724940207") # [cite: 3, 8, 12]
    st.write("[LinkedIn Profile](https://www.linkedin.com/in/john-muya)") # [cite: 4]

# 3. Professional Summary
st.markdown("---")
st.write("### Professional Profile")
st.write("""
I am a person of integrity, reliable, and resilient, with a genuine enthusiasm for analytical chemistry 
and quality control[cite: 14, 17]. My objective is to contribute expertise where precision, accuracy, 
and a commitment to excellence are valued[cite: 17].
""")

# 4. Skills & Expertise
st.markdown("---")
st.header("Core Competencies")
col_s1, col_s2, col_s3 = st.columns(3)

with col_s1:
    st.write("**Laboratory Analysis**")
    st.write("- HPLC & UV-Vis [cite: 19]")
    st.write("- FTIR Spectrophotometry [cite: 19]")
    st.write("- Method Validation [cite: 19]")

with col_s2:
    st.write("**Quality & Compliance**")
    st.write("- WHO/GMP Guidelines [cite: 21, 34]")
    st.write("- CAPA & Change Control [cite: 23, 38]")
    st.write("- Internal Auditing [cite: 23, 40]")

with col_s3:
    st.write("**Technical Oversight**")
    st.write("- Water System Management [cite: 22]")
    st.write("- Resin Regeneration [cite: 22]")
    st.write("- RO Membrane Descaling [cite: 22]")

# 5. Work Experience
st.markdown("---")
st.header("Professional Experience")

# Current Role
with st.expander("Validation Officer | Sphinx Pharmaceuticals Ltd (July 2025 - Present)", expanded=True):
    st.write("""
    - Plan and execute process and cleaning validation in accordance with GMP/WHO guidelines[cite: 31, 34].
    - Maintain Master Validation Plans (MVPs) and Standard Operating Procedures (SOPs)[cite: 35, 36].
    - Coordinate equipment qualification (IQ/OQ/PQ) for air and water systems[cite: 34, 37].
    """)

# Previous Role
with st.expander("Quality Control Analyst | Sphinx Pharmaceuticals Ltd (March 2024 - June 2025)"):
    st.write("""
    - Conducted routine analysis of raw materials and finished products using HPLC and FTIR[cite: 44, 47].
    - Calibrated laboratory instruments including pH meters and spectrophotometers[cite: 50].
    - Mentored junior staff and interns on analytical techniques[cite: 54].
    """)

# Inspection Role
with st.expander("Inspection Clerk | SGS Kenya Limited (June 2022 - March 2023)"):
    st.write("""
    - Verified merchandise against invoice documents to ensure inventory accuracy[cite: 65, 67, 68].
    - Conducted thorough inspections of items to ensure compliance with quality standards[cite: 73].
    """)

# 6. Education & Training
st.markdown("---")
col_edu, col_cert = st.columns(2)

with col_edu:
    st.header("Education")
    st.write("**Diploma in Analytical Chemistry**")
    st.write("Technical University of Mombasa (2018-2021) [cite: 27, 30]")

with col_cert:
    st.header("Certifications")
    st.write("- Good Manufacturing Practices (GMP) [cite: 81]")
    st.write("- Good Documentation Practices (GDP) [cite: 81]")
    st.write("- Advanced Data Analysis (Microsoft Excel) [cite: 81]")

# 7. Sidebar for Projects & Contact
st.sidebar.title("Digital Brand & Projects")
st.sidebar.info("**Krokuta Brand:** Digital content creation focused on African folklore and hyenas.")
st.sidebar.success("**Python Logic:** Developing scripts for lab automation and data handling.")

if st.sidebar.button("Show References"):
    st.sidebar.write("**Samuel Muriuki** (Hope Labs Group) [cite: 83]")
    st.sidebar.write("**Faith Mutiso** (Sphinx Pharmaceuticals) [cite: 83]")
