from fastapi import FastAPI
from app.schema import CropInput, CropOutput
from app.model import predict_crop

app = FastAPI(title="Crop Recommendation API")

@app.get("/")
def root():
    return {"message": "Welcome to the Crop Recommendation API!"}

@app.post("/predict", response_model=CropOutput)
def predict(data: CropInput):
    crop = predict_crop(data)
    return {"crop": crop}