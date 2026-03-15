# Crop Recommendation API

ML-powered REST API that recommends the optimal crop based on soil and
environmental conditions. Built with scikit-learn and FastAPI.

## Features
- Random Forest classifier trained on soil/climate features
- REST API endpoint for real-time predictions
- EDA notebook with feature importance analysis

## Tech stack
Python · scikit-learn · FastAPI · Pandas · Jupyter

## How to run
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Then open `http://localhost:8000/docs` for the interactive API docs.

## Project structure
```
crop-recommendation/
├── app/                 # FastAPI application
├── data/                # Dataset
├── notebooks/           # EDA and model training
└── requirements.txt
```
