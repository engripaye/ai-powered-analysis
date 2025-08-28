from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Load Hugging Face sentiment model
sentiment_pipeline = pipeline("sentiment-analysis")

app = FastAPI()

# Request body schema
class TextRequest(BaseModel):
    text: str

@app.post("/analyze")
def analyze_sentiment(request: TextRequest):
    result = sentiment_pipeline(request.text)[0]
    return {"label": result["label"], "score": result["score"]}
