
from fastapi import FastAPI
from transformers import pipeline

#create FastAPI app
app = FastAPI()

# loads pre-trained sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis")


@app.get("/")
def home():
    return {"message": "ML API is running"}

@app.post("/predict")
def predict(text: str):
    """
    Accepts a text string, runs sentiment analysis,
    and returns the prediction.
    """
    result = sentiment_pipeline(text)
    return {"input": text, "result": result}