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
- README.md # This file


Installation and Set Up

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
- Swagger UI: [http://localhost:8000/docs](url)

- ReDoc: [http://localhost:8000/redoc](url)


