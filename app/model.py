import joblib
import numpy as np
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..\model\crop_model.pkl")
model = joblib.load(MODEL_PATH)

def predict_crop(data):
    features = np.array([[data.N, data.P, data.K, data.temperature, data.humidity, data.ph, data.rainfall]])
    prediction = model.predict(features)
    return prediction[0]
