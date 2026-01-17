from transformers import pipeline

classifier = pipeline("sentiment-analysis")

def detect_emotion(text):
    result = classifier(text)[0]
    return {
        "label": result["label"],
        "confidence": round(result["score"], 2)
    }
