# Rexa ATS Resume Scanner Backend

This is the backend API for the Rexa ATS Resume Scanner, a tool that analyzes resume content against job descriptions to provide a match score and actionable feedback. Built with Flask and designed to integrate seamlessly with the Netlify-hosted frontend.

## 🚀 Live Demo
Frontend: [https://rexa-ats-scan.netlify.app](https://rexa-ats-scan.netlify.app)  
Backend: _Coming soon via Render_

---

## 🔧 Features

- `/scan` endpoint for resume analysis
- Keyword matching between resume and job description
- CORS-enabled for frontend compatibility
- Lightweight and easy to deploy

---

## 🛠️ Tech Stack

- Python 3
- Flask
- Flask-CORS

---

## 📦 Installation

```bash
git clone https://github.com/your-username/rexa-backend.git
cd rexa-backend
pip install -r requirements.txt
python main.py
