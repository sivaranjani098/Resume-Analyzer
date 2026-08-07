import streamlit as st
from pdf_reader import extract_text_from_pdf
from gemini_analyzer import analyze_resume

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.caption("Upload your resume and receive AI-powered ATS feedback.")

# Upload Resume
uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# 👇 Add this here
job_description = st.text_area(
    "Paste Job Description (Optional)",
    height=200
)

if uploaded_file:

    st.success("✅ Resume uploaded successfully")

    resume_text = extract_text_from_pdf(uploaded_file)

    if st.button("Analyze Resume"):

        with st.spinner("Analyzing Resume..."):

            result = analyze_resume(
                resume_text,
                job_description
            )

        st.success("Analysis Completed")

        st.markdown(result)