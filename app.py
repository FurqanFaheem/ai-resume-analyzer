import streamlit as st
from utils import extract_text_from_pdf, extract_text_from_txt, extract_keywords, match_score
import os
st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("📄 AI Resume Analyzer")
st.markdown("Upload your resume and a job description to see how well they match.")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
jd_file = st.file_uploader("Upload Job Description (TXT)", type=["txt"])

if resume_file and jd_file:
    resume_path = os.path.join("resume_samples", resume_file.name)
    jd_path = os.path.join("job_descriptions", jd_file.name)

    os.makedirs("resume_samples", exist_ok=True)
    os.makedirs("job_descriptions", exist_ok=True)

    with open(resume_path, "wb") as f:
        f.write(resume_file.getbuffer())
    with open(jd_path, "wb") as f:
        f.write(jd_file.getbuffer())
    resume_text = extract_text_from_pdf(resume_path)
    jd_text = extract_text_from_txt(jd_path)
    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(jd_text)
    score, common_keywords = match_score(resume_keywords, jd_keywords)
    st.subheader("✅ Analysis Result")
    st.write(f"**Match Score:** {score}%")
    st.write(f"**Common Keywords:** {', '.join(common_keywords)}")
    st.write(f"**Resume Keywords:** {', '.join(resume_keywords)}")
    st.write(f"**Job Description Keywords:** {', '.join(jd_keywords)}")

    if score >= 70:
        st.success("🎉 Great match! You're likely a strong fit.")
        st.write("Consider further customizing your resume to reflect additional key skills or experience.")
    elif score >= 40:
        st.warning("⚠️ Decent match, but room for improvement.")
        st.write("Try adding more relevant keywords from the job description.")
    else:
        st.error("❌ Low match. Consider tailoring your resume more.")
        st.write("Focus on incorporating key terms and skills mentioned in the job description.")