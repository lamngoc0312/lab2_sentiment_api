"""LAB-2: English sentiment analysis API powered by a Hugging Face model."""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator
from transformers import pipeline

MODEL_ID = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"
classifier = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Load the model once when the server starts."""
    global classifier
    try:
        classifier = pipeline("text-classification", model=MODEL_ID, device=-1)
        print("Model loaded successfully!")
    except Exception:
        classifier = None
        logging.exception("Failed to load Hugging Face model")
    yield
    classifier = None


app = FastAPI(
    title="Sentiment Analysis API",
    description="Analyze the sentiment of English text using a Hugging Face model.",
    version="1.0.0",
    lifespan=lifespan,
)


class PredictRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=1000)

    @field_validator("text")
    @classmethod
    def clean_text(cls, value: str) -> str:
        text = value.strip()
        if not text:
            raise ValueError("Text cannot be blank")
        return text


@app.get("/")
def home():
    return {
        "message": "Welcome to the Sentiment Analysis API",
        "model": MODEL_ID,
        "endpoints": ["GET /", "GET /health", "POST /predict"],
    }


@app.get("/health")
def health():
    if classifier is None:
        raise HTTPException(status_code=503, detail="AI model is not ready")
    return {"status": "ok", "model": MODEL_ID}


@app.post("/predict")
def predict(request: PredictRequest):
    if classifier is None:
        raise HTTPException(status_code=503, detail="AI model is not ready")
    try:
        result = classifier(request.text, truncation=True)[0]
    except Exception:
        logging.exception("Model inference failed")
        raise HTTPException(status_code=500, detail="Model inference failed")
    return {
        "input": request.text,
        "label": result["label"],
        "score": round(float(result["score"]), 4),
        "model": MODEL_ID,
    }
