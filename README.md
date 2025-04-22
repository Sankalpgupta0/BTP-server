# Resume Processing Server

This is a Flask server that handles resume uploads and processing.

## Setup

1. Create a Python virtual environment (recommended):
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

1. Make sure your virtual environment is activated
2. Run the server:
```bash
python app.py
```

The server will start on http://localhost:5000

## API Endpoints

### POST /api/upload-resume
Uploads and processes a resume file.

- Request: Multipart form data with 'resume' file
- Supported file types: PDF, DOC, DOCX
- Response: JSON with file details and processed summary

Example response:
```json
{
    "message": "Resume processed successfully",
    "file": {
        "filename": "1234567890-resume.pdf",
        "path": "uploads/1234567890-resume.pdf",
        "size": 12345
    },
    "summary": {
        "contact_info": "...",
        "skills": ["..."],
        "education": ["..."],
        "experience": ["..."],
        "projects": ["..."],
        "certifications": ["..."]
    }
}
``` "# server" 
