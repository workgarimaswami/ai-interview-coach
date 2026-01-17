import whisper
import tempfile

model = whisper.load_model("base")

def transcribe_audio(audio_bytes: bytes):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_bytes)
        tmp.flush()
        result = model.transcribe(tmp.name)

    return result["text"]
