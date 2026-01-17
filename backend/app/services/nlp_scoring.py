from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

IDEAL_ANSWER = "I am a motivated professional with strong problem solving skills."

def score_answer(text):
    emb_user = model.encode(text, convert_to_tensor=True)
    emb_ideal = model.encode(IDEAL_ANSWER, convert_to_tensor=True)

    similarity = util.cos_sim(emb_user, emb_ideal).item()

    return {
        "content_score": round(similarity, 2),
        "feedback": "Improve clarity and structure" if similarity < 0.6 else "Good answer"
    }
