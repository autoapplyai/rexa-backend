from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Allow requests from Netlify

@app.route('/scan', methods=['POST'])
def scan_resume():
    data = request.get_json()
    resume_text = data.get('resumeText', '')
    job_desc = data.get('jobDesc', '')

    # Dummy scoring logic
    score = min(len(set(resume_text.lower().split()) & set(job_desc.lower().split())) * 2, 100)

    return jsonify({
        'status': 'Scan complete',
        'score': score,
        'feedback': 'Your resume matches key terms from the job description.'
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
