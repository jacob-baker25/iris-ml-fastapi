# ML Practice API

- A FastAPI-based project for experimenting with machine learning workflows, APIs, and deployment. This repository contains code for serving ML models via a lightweight, high-performance REST API.

Features: 
- High-Performance API: Utilizes FastAPI for an exceptionally fast and efficient API.
- Modular Design: Built for easy extension and customization.
- ML Inference Endpoints: Includes pre-built endpoints to deploy machine learning models quickly.
- Automatic API Docs: Integrates Swagger UI & ReDoc for interactive, auto-generated documentation.
- Example Model: Features a pre-integrated ML model to demonstrate functionality.

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


