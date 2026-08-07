import os
import google.generativeai as genai
from dotenv import load_dotenv
from prompts import resume_prompt

# Load .env file
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-flash-latest")


def analyze_resume(resume_text, job_description=""):

    prompt = resume_prompt.format(
        resume=resume_text,
        jd=job_description
    )

    response = model.generate_content(prompt)

    return response.text