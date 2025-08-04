import streamlit as st
from career_generator import generate_career_paths
from skill_roadmap import generate_skill_roadmap
from resume_builder import build_resume

st.set_page_config(page_title="FuturePath AI", layout="centered")
st.title("🚀 FuturePath AI")

st.sidebar.title("Select Feature")
feature = st.sidebar.radio("Choose one:", [
    "Smart Career Path Generator",
    "Skill Roadmap Generator",
    "AI Resume Builder"
])

if feature == "Smart Career Path Generator":
    st.header("🎯 Smart Career Path Generator")
    interests = st.text_input("What are your interests?")
    skills = st.text_input("What skills do you already have?")
    education = st.selectbox("Your current education level:", ["10th", "12th", "Diploma", "Graduate", "Postgraduate"])

    if st.button("Generate"):
        if interests and skills:
            with st.spinner("Generating career paths..."):
                result = generate_career_paths(interests, skills, education)
                st.success("Here are your recommended career paths:")
                st.markdown(result)
        else:
            st.warning("Please enter both interests and skills.")

elif feature == "Skill Roadmap Generator":
    st.header("📚 Skill Roadmap Generator")
    career = st.text_input("Enter your dream career (e.g., Data Scientist, AI Engineer)")

    if st.button("Show Roadmap"):
        if career:
            with st.spinner("Generating skill roadmap..."):
                roadmap = generate_skill_roadmap(career)
                st.success("Here’s your learning roadmap:")
                st.markdown(roadmap)
        else:
            st.warning("Please enter a career goal.")

elif feature == "AI Resume Builder":
    st.header("📄 AI Resume Builder")

    name = st.text_input("Full Name")
    summary = st.text_area("Professional Summary")
    skills = st.text_input("Skills (comma-separated)")
    education = st.text_area("Education Background")
    experience = st.text_area("Work Experience")

    if st.button("Generate Resume PDF"):
        if name and summary and skills and education:
            build_resume(name, summary, skills, education, experience)
            st.success("✅ Resume saved as `resume.pdf`")
            with open("resume.pdf", "rb") as file:
                st.download_button("📥 Download Resume", file, file_name="resume.pdf", mime="application/pdf")
        else:
            st.warning("Please fill in all required fields.")
