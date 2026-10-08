# CardioAI ❤️

A full-stack heart disease risk prediction app. A **React + Vite + Tailwind** frontend collects patient health data and a **FastAPI** backend serves predictions from a trained **Logistic Regression** model (scikit-learn).

> ⚠️ **Disclaimer:** CardioAI is an educational/demo project. It is **not** a medical device and must not be used for diagnosis or treatment decisions. Always consult a qualified healthcare professional.

---

## Features

- Predicts heart disease risk (%) from 13 clinical features
- Risk categories: **Low**, **Moderate**, **High**, **Critical**, each with a guidance note
- Returns risk %, healthy %, and model confidence
- Input validation with Pydantic (sensible medical ranges)
- Health-check endpoints for monitoring
- Modern UI with Tailwind CSS, Lucide icons and custom animations (heartbeat, floating blobs, shimmer)

## Tech Stack

| Layer    | Technology                                                        |
| -------- | ----------------------------------------------------------------- |
| Frontend | React 19, Vite, Tailwind CSS 3, PostCSS, Lucide React, Oxlint     |
| Backend  | FastAPI, Uvicorn, Pydantic 2                                      |
| ML       | scikit-learn (Logistic Regression), joblib, NumPy                 |

## Project Structure

```
.
├── backend/
│   ├── main.py                    # FastAPI app + /predict endpoint
│   ├── heart_disease_model.pkl    # Trained model (from Colab notebook)
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   ├── .oxlintrc.json
│   └── src/
│       └── main.jsx               # React entry point
└── README.md
```

> Adjust the layout above if your folders are named differently.

## Prerequisites

- **Node.js** 20+ and npm
- **Python** 3.10+

## Getting Started

### 1. Backend (FastAPI)

```bash
cd backend

# (recommended) create a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt

python main.py
```

The API runs at **http://localhost:8000**. Interactive docs are available at **http://localhost:8000/docs**.

> Make sure `heart_disease_model.pkl` sits in the same folder as `main.py`. The package versions in `requirements.txt` are pinned (notably `scikit-learn==1.6.1`) to match the version used to train the model; a mismatch can cause load errors.

### 2. Frontend (React + Vite)

```bash
cd frontend
npm install
npm run dev
```

The app runs at **http://localhost:5173** (Vite default).

### Available Frontend Scripts

| Command           | Description                    |
| ----------------- | ------------------------------ |
| `npm run dev`     | Start the dev server with HMR  |
| `npm run build`   | Create a production build      |
| `npm run preview` | Preview the production build   |
| `npm run lint`    | Lint the code with Oxlint      |

## API Reference

### `GET /`
Service info and model metadata.

```json
{
  "service": "CardioAI Backend",
  "status": "online",
  "model_loaded": true,
  "model_type": "LogisticRegression",
  "accuracy": { "train": 0.8524, "test": 0.8049 }
}
```

### `GET /health`
Returns `healthy` when the model is loaded, otherwise `degraded`.

### `POST /predict`
Predict risk for one patient.

**Request body**

```json
{
  "age": 54,
  "sex": 1,
  "cp": 0,
  "trestbps": 130,
  "chol": 246,
  "fbs": 0,
  "restecg": 1,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 1.0,
  "slope": 1,
  "ca": 0,
  "thal": 2
}
```

**Response**

```json
{
  "risk": 42.3,
  "healthy": 57.7,
  "confidence": 57.7,
  "prediction": 1,
  "label": "MODERATE RISK",
  "status": "warning",
  "note": "Some risk factors present. Lifestyle changes advised."
}
```

**Example with cURL**

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"age":54,"sex":1,"cp":0,"trestbps":130,"chol":246,"fbs":0,"restecg":1,"thalach":150,"exang":0,"oldpeak":1.0,"slope":1,"ca":0,"thal":2}'
```

**Errors:** `422` for invalid input, `503` if the model failed to load, `500` if prediction fails.

## Input Features

| Field      | Description                                   | Valid range |
| ---------- | --------------------------------------------- | ----------- |
| `age`      | Age in years                                  | 1 – 120     |
| `sex`      | 0 = female, 1 = male                          | 0 – 1       |
| `cp`       | Chest pain type                               | 0 – 3       |
| `trestbps` | Resting blood pressure (mm Hg)                | 80 – 250    |
| `chol`     | Serum cholesterol (mg/dl)                     | 100 – 600   |
| `fbs`      | Fasting blood sugar > 120 mg/dl (1 = true)    | 0 – 1       |
| `restecg`  | Resting ECG results                           | 0 – 2       |
| `thalach`  | Maximum heart rate achieved                   | 60 – 250    |
| `exang`    | Exercise-induced angina (1 = yes)             | 0 – 1       |
| `oldpeak`  | ST depression induced by exercise             | 0.0 – 10.0  |
| `slope`    | Slope of the peak exercise ST segment         | 0 – 2       |
| `ca`       | Number of major vessels colored by fluoroscopy| 0 – 4       |
| `thal`     | Thalassemia type                              | 0 – 3       |

The feature order is fixed and **must match the training order** (as listed above).

## Risk Levels

The model's disease probability is mapped to a category:

| Risk (%) | Label          | Guidance                                              |
| -------- | -------------- | ----------------------------------------------------- |
| < 30     | LOW RISK       | Indicators within healthy range                       |
| 30 – 55  | MODERATE RISK  | Some risk factors; lifestyle changes advised          |
| 55 – 75  | HIGH RISK      | Consult a cardiologist for detailed evaluation        |
| ≥ 75     | CRITICAL RISK  | Seek immediate medical attention                      |

## Model

- **Algorithm:** Logistic Regression (scikit-learn)
- **Accuracy:** 85.24% train / 80.49% test
- **Features:** 13 (UCI-style heart disease dataset)
- **Label encoding:** in this dataset `target = 0` → disease, `target = 1` → healthy, so the backend uses `predict_proba()[0]` as the disease risk.

## Configuration Notes

- **CORS** is currently open (`allow_origins=["*"]`) for development. Restrict it to your frontend's origin before deploying.
- The backend listens on `0.0.0.0:8000`; update the API base URL in the frontend if you change the host or port.

## Deployment

1. **Frontend:** run `npm run build` and host the `dist/` folder (Vercel, Netlify, etc.).
2. **Backend:** deploy with Uvicorn/Gunicorn on a platform such as Render, Railway, or a VPS, and restrict CORS to your frontend domain.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes and open a pull request

## License

Add your license here (e.g., MIT).
