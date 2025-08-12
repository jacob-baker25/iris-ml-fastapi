"""
This FastAPI application serves a machine learning model trained on the 
Iris dataset to predict flower species from measurements.

How it works:
1. Loads a pre-trained Logistic Regression model from 'iris_model.joblib' 
   (created by the training script).
2. Defines an API endpoint to accept flower measurements:
   - sepal_length (float)
   - sepal_width  (float)
   - petal_length (float)
   - petal_width  (float)
3. When a POST request is sent to /predict with these measurements,
   the model predicts the species class (0=Setosa, 1=Versicolor, 2=Virginica)
   and returns the numeric class as JSON.
4. Includes a root GET endpoint ("/") for a simple "API is running" health check.

This allows the model to be accessed remotely without retraining, making
predictions on new data through a web API.
"""

from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# load model at startup
model = joblib.load("iris_model.joblib")

#create FastAPI app
app = FastAPI()

class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.get("/")
def read_root():
    return {"message": "ML API is running"}

@app.post("/predict")
def predict(features: IrisFeatures):
    data = [[
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width
    ]]
    prediction = model.predict(data)[0]
    species = ["Setosa", "Versicolor", "Virginica"]
    return {"predicted_species": species[prediction]}
