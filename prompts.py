resume_prompt = """
You are an ATS Resume Analyzer.

Compare the resume with the job description.

Return:

1. ATS Score (0-100)
2. Match Percentage
3. Resume Summary
4. Strengths
5. Missing Skills
6. Resume Weaknesses
7. Improvement Suggestions

Resume:
{resume}

Job Description:
{jd}
"""