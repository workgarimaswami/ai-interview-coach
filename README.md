# AI Interview Coach 🎤🤖

An end-to-end AI-powered interview practice platform that analyzes spoken answers using **speech-to-text**, **NLP content scoring**, **emotion detection**, and **audio confidence metrics**, then returns actionable feedback to help candidates improve.

---

## ✨ Key Features

* 🎙️ **Voice-based interview practice** (upload/record audio)
* 🧠 **Automatic transcription** using Whisper
* 📝 **NLP content scoring** (clarity, structure, relevance)
* 😊 **Emotion & sentiment analysis**
* 🗣️ **Speaking metrics** (duration, speech rate, confidence)
* 📊 **Structured feedback** with improvement tips

---

## 🏗️ Architecture

```
Frontend (React)
   │
   ├── Recorder (browser audio)
   │
   ▼
Backend (FastAPI)
   ├── /interview/analyze
   │   ├── Whisper (STT)
   │   ├── NLP Scoring (Transformers)
   │   ├── Emotion Detection
   │   └── Audio Features (FFmpeg)
   ▼
JSON Response (scores + feedback)
```

---

## 🧰 Tech Stack

**Backend**

* Python, FastAPI
* Whisper (speech-to-text)
* HuggingFace Transformers
* librosa / soundfile
* FFmpeg (audio decoding)

**Frontend**

* React
* Fetch API / Axios

**ML / NLP**

* Sentence Transformers
* Sentiment analysis pipelines

---

## 🚀 Getting Started

### Prerequisites

* Python 3.10+
* Node.js 18+
* FFmpeg installed and available on PATH

### Backend Setup

```bash
cd backend
python -m venv .venv
.\.venv\Scripts\activate  # Windows
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

### Frontend Setup

```bash
cd frontend
npm install
npm start
```

---

## 🧪 Example API Response

```json
{
  "transcript": "Hello, I am a software engineering graduate...",
  "emotion": {"label": "POSITIVE", "confidence": 1.0},
  "audio_metrics": {
    "duration_sec": 22.57,
    "speech_rate": 107.67,
    "confidence_score": 0.72
  },
  "nlp_score": {
    "content_score": 0.41,
    "feedback": "Improve clarity and structure"
  }
}
```

## 📄 License

MIT

---

## 🙌 Author

Built by **Garima** — showcasing full-stack ML engineering with real-world audio + NLP pipelines.
