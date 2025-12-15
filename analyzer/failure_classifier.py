
#Determines the primary cause of failure in a RAG response.


def classify_failure(grounding: dict, retrieval: dict):
    if retrieval["relevance_score"] == 0.0:
        return "retrieval_failure"

    if grounding["grounding_score"] == 0.0:
        return "hallucination"

    if grounding["grounding_score"] < 0.7:
        return "partial_grounding"

    return "no_failure_detected"
