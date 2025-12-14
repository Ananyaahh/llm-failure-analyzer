#Grounding analyzer,Checks whether an answer is supported by retrieved context.
def analyze_grounding(answer: str, retrieved_docs: list):
    return {
        "grounding_score": None,
        "unsupported_claims": []
    }
