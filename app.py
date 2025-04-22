from flask import Flask, request, jsonify
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from summarizer import extract_text_from_resume, analyze_resume_with_model
from flask_cors import CORS

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

# Initialize Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0,
    max_completion_tokens=100,
)

@app.route('/', methods=['GET'])
def main():
    return jsonify({'message': 'Hello, World!'})

@app.route('/analyze', methods=['POST'])
def analyze_resume():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400

    text = extract_text_from_resume(file)
    if text.startswith("Unsupported"):
        return jsonify({'error': text}), 400

    response = analyze_resume_with_model(text, model)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
