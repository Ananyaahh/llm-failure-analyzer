frfrom rag_baseline.baseline import run_rag
from analyzer.grounding import analyze_grounding
from analyzer.retrieval_quality import analyze_retrieval

def analyze_prompt(prompt: str):
    rag_output = run_rag(prompt)

    grounding = analyze_grounding(
        answer=rag_output["answer"],
        retrieved_docs=rag_output["retrieved_docs"]
    )

    retrieval = analyze_retrieval(
        query=prompt,
        retrieved_docs=rag_output["retrieved_docs"]
    )

    return {
        "prompt": prompt,
        "analysis": {
            "grounding": grounding,
            "retrieval_quality": retrieval
        }
    }
