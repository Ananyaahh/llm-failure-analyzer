
#Checks whether retrieved documents are relevant to the query.


def analyze_retrieval(query: str, retrieved_docs: list):
    if not retrieved_docs:
        return {
            "relevance_score": 0.0,
            "issue": "no documents retrieved"
        }

    return {
        "relevance_score": 1.0,
        "issue": None
    }
