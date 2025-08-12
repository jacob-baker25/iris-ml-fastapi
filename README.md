# Iris Species Classification API

This project provides a RESTful API built with **FastAPI** that uses a trained **Logistic Regression** machine learning model to classify iris flowers based on their sepal and petal measurements.

---

## Features

- Trains a Logistic Regression model on the classic Iris dataset.
- Saves the trained model using **joblib**.
- Loads the saved model in a FastAPI app.
- Provides a POST `/predict` endpoint to classify iris flower species from input measurements.
- Returns the predicted species name: *Setosa*, *Versicolor*, or *Virginica*.
- Includes a simple GET `/` health check endpoint.

---

## Project Structure

- main.py # FastAPI application code
- train_model.py # Script to train and save the ML model
- iris_model.joblib # Saved Logistic Regression model file
- requirements.txt # Python dependencies
- Dockerfile # Docker image build instructions
- .dockerignore # Files/folders to ignore in Docker build
- README.md # This file

---

## Installation and Set Up

1. Clone Repository:
```bash
git clone https://github.com/jacob-baker25/ml-practice.git  
cd ml-practice
```
2. Create and activate virtual environment
```bash
python -m venv venv
for Windows
venv\Scripts\activate
for macOS/Linux
source venv/bin/activate
```
3. Install dependencies 
```bash
pip install -r requirements.txt
```
Running the API:
```bash
uvicorn app.main:app --reload
```
- The API will run on http://localhost:8000.

- The root endpoint `/` returns a simple status message.

- The `/predict` endpoint accepts POST requests with JSON payload containing iris flower measurements.

---

# Training the Model

If you want to retrain the model or update it:

```bash
python train_model.py
```
This will:

 - Load the Iris dataset from scikit-learn.

 - Train a Logistic Regression model.

 - Save the trained model as iris_model.joblib.

---

# API Usage
## Health check  
Endpoint: `GET /`

Response:
```json
{
  "message": "ML API is running"
}
```

## Predict species  
Endpoint: `POST /predict`

Request JSON body:

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```
## Response JSON:  

```json
{
  "predicted_species": "Setosa"
}
```

# Docker Support (optional)
To build and run the API in a Docker container:

```bash
docker build -t iris-api .
docker run -p 8000:8000 iris-api
```
The API will be accessible at http://localhost:8000
