# Document Summarizer Assignment
# Document Summarizer via Google Drive Integration

## Features

- OAuth2 Google Login
- Access Google Drive Folder
- Download PDF, DOCX, TXT files
- Extract document text
- AI Summarization using OpenAI GPT
- HTML Dashboard
- CSV Export
- PDF Export

## Setup

1. Create Google Cloud Project

2. Enable Drive API

3. Download credentials.json

4. Install packages

pip install -r requirements.txt

5. Add OpenAI API Key

summarizer.py

6. Add Google Drive Folder ID

app.py

7. Run

uvicorn app:app --reload

Open:

http://localhost:8000/report
