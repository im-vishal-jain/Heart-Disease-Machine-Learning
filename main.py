"""
CardioAI Backend — FastAPI + Real LogisticRegression Model
Uses the trained heart_disease_model.pkl from Colab notebook.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import joblib
import numpy as np
import os

# ============================================================
# APP INIT
# ============================================================
app = FastAPI(title="CardioAI Backend", version="1.0.0")

# CORS — React frontend se connect karne ke liye
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================
# LOAD TRAINED MODEL
# ============================================================
MODEL_PATH = os.path.join(os.path.dirname(__file__), "heart_disease_model.pkl")

try:
    model = joblib.load(MODEL_PATH)
    print(f"[OK] Model loaded: {MODEL_PATH}")
    print(f"     Classes: {model.classes_}")
    print(f"     Expected features: {model.n_features_in_}")
except Exception as e:
    print(f"[ERROR] Failed to load model: {e}")
    model = None


# ============================================================
# REQUEST SCHEMA (13 features — same as notebook)
# ============================================================
class PatientData(BaseModel):
    age: int = Field(..., ge=1, le=120)
    sex: int = Field(..., ge=0, le=1)
    cp: int = Field(..., ge=0, le=3)
    trestbps: int = Field(..., ge=80, le=250)
    chol: int = Field(..., ge=100, le=600)
    fbs: int = Field(..., ge=0, le=1)
    restecg: int = Field(..., ge=0, le=2)
    thalach: int = Field(..., ge=60, le=250)
    exang: int = Field(..., ge=0, le=1)
    oldpeak: float = Field(..., ge=0.0, le=10.0)
    slope: int = Field(..., ge=0, le=2)
    ca: int = Field(..., ge=0, le=4)
    thal: int = Field(..., ge=0, le=3)


# ============================================================
# RISK CATEGORIZATION
# ============================================================
def risk_meta(risk: float) -> dict:
    if risk < 30:
        return {"label": "LOW RISK", "status": "success",
                "note": "Cardiovascular indicators within healthy range."}
    if risk < 55:
        return {"label": "MODERATE RISK", "status": "warning",
                "note": "Some risk factors present. Lifestyle changes advised."}
    if risk < 75:
        return {"label": "HIGH RISK", "status": "warning",
                "note": "Consult a cardiologist for detailed evaluation."}
    return {"label": "CRITICAL RISK", "status": "danger",
            "note": "Seek immediate medical attention."}


# ============================================================
# ROUTES
# ============================================================
@app.get("/")
def root():
    return {
        "service": "CardioAI Backend",
        "status": "online",
        "model_loaded": model is not None,
        "model_type": "LogisticRegression",
        "accuracy": {"train": 0.8524, "test": 0.8049},
    }


@app.get("/health")
def health():
    return {
        "status": "healthy" if model else "degraded",
        "model_loaded": model is not None,
    }


@app.post("/predict")
def predict(data: PatientData):
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")

    # Feature order MUST match training:
    # age, sex, cp, trestbps, chol, fbs, restecg,
    # thalach, exang, oldpeak, slope, ca, thal
    features = np.array([[
        data.age, data.sex, data.cp, data.trestbps, data.chol,
        data.fbs, data.restecg, data.thalach, data.exang,
        data.oldpeak, data.slope, data.ca, data.thal,
    ]], dtype=float)

    try:
        prediction = int(model.predict(features)[0])
        proba = model.predict_proba(features)[0]

        # In this dataset: target=0 → Disease, target=1 → Healthy
        disease_risk = float(proba[0] * 100)
        healthy_prob = float(proba[1] * 100)
        confidence = max(disease_risk, healthy_prob)

        meta = risk_meta(disease_risk)

        return {
            "risk": round(disease_risk, 1),
            "healthy": round(healthy_prob, 1),
            "confidence": round(confidence, 1),
            "prediction": prediction,
            "label": meta["label"],
            "status": meta["status"],
            "note": meta["note"],
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {e}")


# ============================================================
# RUN (reload=False to avoid warning)
# ============================================================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)