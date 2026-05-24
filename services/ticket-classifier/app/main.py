"""FastAPI ticket classification service."""

from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

from app.pipeline import classify

app = FastAPI(title="Acme Support Ticket Classifier")


class ClassifyRequest(BaseModel):
    text: str


class ClassifyResponse(BaseModel):
    category: str
    confidence: int
    preprocessed_text: str


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/classify", response_model=ClassifyResponse)
def classify_ticket(request: ClassifyRequest) -> ClassifyResponse:
    result = classify(request.text)
    return ClassifyResponse(**result)
