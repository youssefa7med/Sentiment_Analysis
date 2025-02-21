import requests
import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Load environment variables
load_dotenv()
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Hugging Face API configuration
API_URL = "https://api-inference.huggingface.co/models/nlptown/bert-base-multilingual-uncased-sentiment"
HEADERS = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}

# FastAPI app initialization
app = FastAPI()

# Request model
class TextInput(BaseModel):
    text: str

# Sentiment analysis function
def sentiment_analysis(text: str):
    payload = {"inputs": text}
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    try:
        return response.json()[0][0]["label"]  # Extract sentiment label
    except (IndexError, KeyError):
        raise HTTPException(status_code=500, detail="Unexpected response format from Hugging Face API")

# FastAPI endpoint
@app.post("/analyze_sentiment/")
def analyze_sentiment(input_data: TextInput):
    sentiment = sentiment_analysis(input_data.text)
    return {"text": input_data.text, "sentiment": sentiment}
