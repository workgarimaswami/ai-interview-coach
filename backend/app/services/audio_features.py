import librosa
import tempfile

def extract_audio_features(audio_bytes: bytes):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_bytes)
        tmp.flush()
        y, sr = librosa.load(tmp.name)

    duration = librosa.get_duration(y=y, sr=sr)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

    confidence_score = min(1.0, float(tempo) / 150)

    return {
        "duration_sec": round(duration, 2),
        "speech_rate": round(float(tempo), 2),
        "confidence_score": round(confidence_score, 2)
    }
