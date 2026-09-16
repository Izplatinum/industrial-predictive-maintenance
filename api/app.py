from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
from pathlib import Path

app = FastAPI(
    title="Industrial Predictive Maintenance API",
    version="1.0"
)

BASE_DIR = Path(__file__).resolve().parent.parent
models_dir = BASE_DIR / "models"

model = joblib.load(
    models_dir / "predictive_maintenance_rf_top10.joblib"
)

features = joblib.load(
    models_dir / "predictive_maintenance_top10_features.joblib"
)


class SensorInput(BaseModel):
    fs1_mean: float
    fs1_std: float
    eps1_mean: float
    ps1_max: float
    eps1_min: float
    eps1_max: float
    ps1_min: float
    ps1_mean: float
    ts1_min: float
    ts1_mean: float


@app.get("/")
def root():
    return {
        "message": "Industrial Predictive Maintenance API is running"
    }


@app.post("/predict")
def predict(data: SensorInput):

    input_df = pd.DataFrame(
        [data.model_dump()]
    )

    input_df = input_df[features]

    prediction = int(
        model.predict(input_df)[0]
    )

    labels = {
        0: "No Leakage",
        1: "Weak Leakage",
        2: "Severe Leakage"
    }

    return {
        "prediction": prediction,
        "status": labels[prediction]
    }