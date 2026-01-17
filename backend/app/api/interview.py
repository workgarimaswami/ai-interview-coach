from fastapi import APIRouter, UploadFile, File
from app.services.speech_to_text import transcribe_audio
from app.services.audio_features import extract_audio_features
from app.services.nlp_scoring import score_answer
from app.services.emotion_detection import detect_emotion
import traceback

router = APIRouter()

@router.post("/analyze")
async def analyze_interview(audio: UploadFile = File(...)):
    try:
        audio_bytes = await audio.read()

        text = transcribe_audio(audio_bytes)
        audio_feats = extract_audio_features(audio_bytes)
        nlp_score = score_answer(text)
        emotion = detect_emotion(text)

        return {
            "transcript": text,
            "emotion": emotion,
            "audio_metrics": audio_feats,
            "nlp_score": nlp_score,
        }

    except Exception as e:
        traceback.print_exc()  # 👈 PRINTS REAL ERROR IN TERMINAL
        return {"error": str(e)}
