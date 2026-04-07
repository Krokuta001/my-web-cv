import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Professional Portfolio", layout="wide")

# 2. Hero Section
st.title("Analytical Chemist | Quality Assurance Professional")
st.write("Specializing in Pharmaceutical Validation, ISO Standards, and Data Logic.")

st.markdown("---")

# 3. Core Expertise (Using Columns for a modern look)
col1, col2 = st.columns(2)

with col1:
    st.header("Technical Standards")
    st.write("- **ISO 17025** (Laboratory Competence)")
    st.write("- **ISO 19011** (Auditing Management)")
    st.write("- **GAMP 5** (V-Model & Compliance)")

with col2:
    st.header("Programming & Data")
    st.write("- **Python:** Logic, Functions, Error Handling")
    st.write("- **Data Science:** Transitioning into Analytics")
    st.write("- **Automation:** Laboratory workflow scripting")

st.markdown("---")

# 4. Professional Projects
st.header("Key Operational Projects")
st.info("Expert oversight of technical water systems, including resin regeneration and RO membrane descaling.")

# 5. Creative Brand
st.sidebar.title("Krokuta Brand")
st.sidebar.write("Exploring African folklore and hyena-themed digital content creation.")
