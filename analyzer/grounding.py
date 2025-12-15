#Grounding analyzer,Checks whether an answer is supported by retrieved context.


from typing import List

def analyze_grounding(answer: str, retrieved_docs: List[str]):
    if not answer.strip():
        return {
            "grounding_score": 0.0,
            "unsupported_claims": ["Empty answer"]
        }

    if not retrieved_docs:
        return {
            "grounding_score": 0.0,
            "unsupported_claims": [answer]
        }

    supported = 0
    unsupported_claims = []

    sentences = [s.strip() for s in answer.split(".") if s.strip()]

    for s in sentences:
        found = any(s.lower() in doc.lower() for doc in retrieved_docs)
        if found:
            supported += 1
        else:
            unsupported_claims.append(s)

    grounding_score = supported / max(len(sentences), 1)

    return {
        "grounding_score": round(grounding_score, 2),
        "unsupported_claims": unsupported_claims
    }
