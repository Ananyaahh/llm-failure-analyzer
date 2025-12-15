# LLM Failure Analyzer for RAG Systems

This project is a diagnostic toolkit for analyzing failure modes in Retrieval-Augmented Generation (RAG) pipelines.

Instead of generating answers, the system inspects RAG outputs to identify:
- hallucinations
- weak grounding
- retrieval failures

It is designed as an internal tool for AI engineers to understand *why* a RAG system fails.

## Running the Analyzer

Install dependencies:
```bash
pip install -r requirements.txt

## What This Project Demonstrates

- Diagnosing hallucinations and grounding failures in RAG systems
- Separating retrieval errors from model errors
- Designing analysis pipelines instead of user-facing chatbots
- Rule-based evaluation logic for LLM outputs
- Clear system decomposition and failure reasoning
