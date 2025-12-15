from fastapi import FastAPI
from analyzer.run_analysis import analyze_prompt

app = FastAPI()

@app.get("/analyze")
def analyze(prompt: str):
    return analyze_prompt(prompt)
