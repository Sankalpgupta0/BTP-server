import pdfplumber

def extract_text_from_resume(file):
    if file.filename.endswith('.txt'):
        return file.read().decode('utf-8')
    elif file.filename.endswith('.pdf'):
        # Use pdfplumber to open and read the PDF
        with pdfplumber.open(file) as pdf:
            text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
            return text
    else:
        return "Unsupported file format."

def analyze_resume_with_model(text, model):
    # Define the prompt for analyzing the resume
    prompt = f"""
    Summarize the following resume text in 200 words. Provide the summary **only in Markdown format**:
    {text}
    """
    # Use the Gemini model to analyze the resume text
    result = model.invoke(prompt)
    return result.content
