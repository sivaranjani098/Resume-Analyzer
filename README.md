# AI Resume Analyzer

## Overview

AI Resume Analyzer is an intelligent web application that evaluates resumes using Google's Gemini AI. The application analyzes resumes against a job description, identifies strengths and weaknesses, provides ATS-friendly suggestions, and generates an overall match score to help job seekers improve their resumes.

## Features

* Upload resumes in PDF format.
* Extract text from uploaded resumes.
* Compare resumes with a job description.
* Calculate resume-job match score.
* Identify missing skills and keywords.
* Generate ATS optimization suggestions.
* Highlight strengths and improvement areas.
* User-friendly web interface built with Streamlit.
* AI-powered analysis using Google Gemini.

## Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **AI Model:** Google Gemini API
* **Libraries:**

  * Streamlit
  * PyPDF2
  * Google Generative AI (Gemini)
  * python-dotenv

## Project Structure

```
Resume-Analyzer/
│── app.py
│── utils.py
│── requirements.txt
│── .env
│── README.md
│── assets/
└── sample_resume.pdf
```

## How It Works

1. Upload your resume in PDF format.
2. Enter the job description (optional but recommended).
3. The application extracts text from the resume.
4. Gemini AI analyzes the resume against the job description.
5. Receive:

   * ATS Match Score
   * Resume Summary
   * Missing Skills
   * Strengths
   * Weaknesses
   * Improvement Suggestions

## Installation

Clone the repository:

```bash
git clone https://github.com/sivaranjani098/Resume-Analyzer.git
```

Navigate to the project folder:

```bash
cd Resume-Analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run app.py
```
## 📸 Screenshots

### Home Page

![Home Page](assets/home.png)

### Resume Upload

![Resume Upload](assets/upload.png)

### Analysis Result

![Analysis Result](assets/analysis.png)
## Future Enhancements

* Support for DOCX resumes.
* Resume grammar and spelling analysis.
* Resume keyword optimization.
* Multiple resume comparison.
* Download analysis report as PDF.
* Resume improvement recommendations.
* Resume template suggestions.

## Use Cases

* Students and fresh graduates.
* Job seekers.
* Career counselors.
* HR professionals.
* Recruitment agencies.
