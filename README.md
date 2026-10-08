<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=34&pause=1200&color=EF4444&center=true&vCenter=true&width=700&lines=%E2%9D%A4%EF%B8%8F+CardioAI;AI-Powered+Heart+Disease+Risk+Assessment;Machine+Learning+%2B+FastAPI+%2B+React" alt="CardioAI typing banner" />

### AI-Powered Heart Disease Risk Assessment Platform

*Enter clinical metrics. Get an instant, explainable cardiovascular risk score.*

<br/>

![React](https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Vite](https://img.shields.io/badge/Vite-8-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.6-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-Frontend-000000?style=for-the-badge&logo=vercel&logoColor=white)
![Render](https://img.shields.io/badge/Render-Backend-46E3B7?style=for-the-badge&logo=render&logoColor=black)

![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)
![Test Accuracy](https://img.shields.io/badge/Test_Accuracy-80.49%25-blue?style=flat-square)

[🚀 Live Demo](#) · [📖 API Docs](#-api-documentation) · [🐛 Report Bug](../../issues) · [✨ Request Feature](../../issues)

</div>

---

> [!WARNING]
> **Medical disclaimer:** CardioAI is an educational and portfolio project. It is **not** a certified medical device and must **not** be used for diagnosis or treatment. Always consult a qualified healthcare professional.

## 📑 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [System Architecture](#-system-architecture)
- [Screenshots](#-screenshots)
- [Machine Learning Workflow](#-machine-learning-workflow)
- [Installation & Local Setup](#-installation--local-setup)
- [API Documentation](#-api-documentation)
- [Folder Structure](#-folder-structure)
- [Deployment Guide](#-deployment-guide)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [Author](#-author)
- [GitHub Stats](#-github-stats)
- [License](#-license)

---

## 🌟 Overview

**CardioAI** is a full-stack **Machine Learning + Healthcare SaaS** application that estimates the likelihood of heart disease from 13 clinical indicators such as age, cholesterol, resting blood pressure, chest pain type, and maximum heart rate.

A **React** dashboard sends patient data to a **FastAPI** REST service, which runs a trained **Logistic Regression** model (scikit-learn) and returns a risk percentage, a risk category, and clinical guidance, all in real time.

| 🎯 Goal | 💡 Approach | 📊 Result |
|---|---|---|
| Early, accessible risk screening | ML model served behind a REST API | **85.24%** train / **80.49%** test accuracy |

---

## ✨ Key Features

| | Feature | Description |
|---|---|---|
| 🧠 | **ML-Based Prediction** | Logistic Regression trained on 13 clinical features |
| ⚡ | **Real-Time Risk Assessment** | Sub-second inference through FastAPI |
| 📊 | **Risk Score Visualization** | Gauge-style score with Low / Moderate / High / Critical bands |
| 🔍 | **Explainable AI Insights** | Feature-contribution view showing which inputs drive the result |
| 🎨 | **Modern SaaS Dashboard** | Clean Tailwind UI with heartbeat, blob and shimmer animations |
| 🧑‍⚕️ | **Patient Management** | Create and manage patient records (PostgreSQL) |
| 🕘 | **Prediction History** | Review past assessments per patient |
| 📈 | **Analytics Dashboard** | Aggregate trends and risk distribution charts |
| 📄 | **PDF Report Generation** | Downloadable assessment reports |
| 📱 | **Responsive Design** | Optimized for desktop, tablet and mobile |
| 🔌 | **REST API Integration** | Documented, validated endpoints with Swagger UI |

> 📌 The core prediction engine, validation, risk categorization and health endpoints are implemented. Patient management, history, analytics and PDF export are part of the product scope and roadmap; see [Future Enhancements](#-future-enhancements).

---

## 🛠 Tech Stack

| Layer | Technologies |
|---|---|
| **Frontend** | React 19, Vite, Tailwind CSS, PostCSS, Lucide React, Oxlint |
| **Backend** | Python, FastAPI, Uvicorn, Pydantic v2 |
| **Machine Learning** | scikit-learn, Pandas, NumPy, joblib |
| **Database** | PostgreSQL |
| **Deployment** | Vercel (frontend), Render (backend) |

---

## 🏗 System Architecture

```mermaid
flowchart LR
    U([👤 User / Clinician]) --> FE

    subgraph Client["🖥 Frontend · Vercel"]
        FE["React + Vite + Tailwind<br/>Dashboard · Forms · Charts"]
    end

    FE -- "HTTPS · JSON" --> API

    subgraph Server["⚙️ Backend · Render"]
        API["FastAPI<br/>Validation (Pydantic)"]
        ML["🧠 Logistic Regression<br/>heart_disease_model.pkl"]
        RISK["Risk Categorization<br/>Low · Moderate · High · Critical"]
        API --> ML --> RISK
    end

    API <--> DB[("🗄 PostgreSQL<br/>Patients · Predictions")]
    RISK --> API
    API -- "risk %, label, note" --> FE
```

<details>
<summary><b>📦 Text version of the diagram</b></summary>

```
┌─────────────────┐    HTTPS/JSON    ┌──────────────────────────────────────┐
│    FRONTEND     │ ───────────────► │               BACKEND                │
│  React · Vite   │                  │  FastAPI ─► Pydantic Validation      │
│  Tailwind CSS   │ ◄─────────────── │     │                                │
│  (Vercel)       │  risk, label,    │     ├─► Logistic Regression (.pkl)   │
└─────────────────┘  confidence      │     ├─► Risk Categorization          │
                                     │     └─► PostgreSQL (history/patients)│
                                     │            (Render)                  │
                                     └──────────────────────────────────────┘
```

</details>

### 🔄 Request Lifecycle

```mermaid
sequenceDiagram
    participant U as User
    participant F as React Frontend
    participant A as FastAPI
    participant M as ML Model
    U->>F: Enter 13 clinical metrics
    F->>A: POST /predict (JSON)
    A->>A: Validate input ranges
    A->>M: predict_proba(features)
    M-->>A: [disease %, healthy %]
    A->>A: Map risk to category
    A-->>F: risk, label, status, note
    F-->>U: Risk gauge + guidance
```

---

## 📸 Screenshots

> Replace the placeholders below with real screenshots stored in `docs/screenshots/`.

| 🏠 Landing Page | 📊 Dashboard |
|---|---|
| ![Landing](docs/screenshots/landing.png) | ![Dashboard](docs/screenshots/dashboard.png) |

| 🩺 Risk Assessment | 📈 Analytics |
|---|---|
| ![Assessment](docs/screenshots/assessment.png) | ![Analytics](docs/screenshots/analytics.png) |

| 🕘 Prediction History | 📄 PDF Report |
|---|---|
| ![History](docs/screenshots/history.png) | ![Report](docs/screenshots/report.png) |

---

## 🧬 Machine Learning Workflow

```mermaid
flowchart LR
    A[📥 Dataset<br/>UCI Heart Disease] --> B[🧹 Cleaning<br/>Pandas]
    B --> C[🔎 EDA<br/>Correlations · Distributions]
    C --> D[⚙️ Feature Selection<br/>13 clinical features]
    D --> E[✂️ Train/Test Split]
    E --> F[🏋️ Train<br/>Logistic Regression]
    F --> G[📏 Evaluate<br/>Accuracy · Metrics]
    G --> H[💾 Export<br/>joblib .pkl]
    H --> I[🚀 Serve<br/>FastAPI /predict]
```

### Model Summary

| Property | Value |
|---|---|
| Algorithm | Logistic Regression (scikit-learn) |
| Input features | 13 |
| Train accuracy | **85.24%** |
| Test accuracy | **80.49%** |
| Serialization | `joblib` |
| Label encoding | `0` = Disease, `1` = Healthy |

### 🩺 Input Features

| Feature | Meaning | Range |
|---|---|---|
| `age` | Age in years | 1 – 120 |
| `sex` | 0 = female, 1 = male | 0 – 1 |
| `cp` | Chest pain type | 0 – 3 |
| `trestbps` | Resting blood pressure (mm Hg) | 80 – 250 |
| `chol` | Serum cholesterol (mg/dl) | 100 – 600 |
| `fbs` | Fasting blood sugar > 120 mg/dl | 0 – 1 |
| `restecg` | Resting ECG result | 0 – 2 |
| `thalach` | Maximum heart rate achieved | 60 – 250 |
| `exang` | Exercise-induced angina | 0 – 1 |
| `oldpeak` | ST depression induced by exercise | 0.0 – 10.0 |
| `slope` | Slope of peak exercise ST segment | 0 – 2 |
| `ca` | Major vessels colored by fluoroscopy | 0 – 4 |
| `thal` | Thalassemia type | 0 – 3 |

### 🚦 Risk Categories

| Risk % | Label | Guidance |
|---|---|---|
| < 30 | 🟢 **LOW RISK** | Indicators within healthy range |
| 30 – 55 | 🟡 **MODERATE RISK** | Some risk factors; lifestyle changes advised |
| 55 – 75 | 🟠 **HIGH RISK** | Consult a cardiologist |
| ≥ 75 | 🔴 **CRITICAL RISK** | Seek immediate medical attention |

---

## ⚙️ Installation & Local Setup

### ✅ Prerequisites

- **Node.js** 20+ and **npm**
- **Python** 3.10+
- **PostgreSQL** 14+ *(only for patient management / history features)*
- **Git**

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/cardioai.git
cd cardioai
```

### 2️⃣ Backend setup (FastAPI)

```bash
cd backend

python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

pip install -r requirements.txt

python main.py
```

| Service | URL |
|---|---|
| API | http://localhost:8000 |
| Swagger UI | http://localhost:8000/docs |
| ReDoc | http://localhost:8000/redoc |

> 💡 Keep `heart_disease_model.pkl` next to `main.py`. Package versions are pinned (especially `scikit-learn==1.6.1`) to match the training environment.

### 3️⃣ Frontend setup (React + Vite)

```bash
cd frontend
npm install
npm run dev
```

App runs at **http://localhost:5173**.

### 4️⃣ Environment variables *(optional / when database is enabled)*

```env
# backend/.env
DATABASE_URL=postgresql://user:password@localhost:5432/cardioai
ALLOWED_ORIGINS=http://localhost:5173

# frontend/.env
VITE_API_URL=http://localhost:8000
```

### 🧰 Useful scripts

| Command | Description |
|---|---|
| `npm run dev` | Start frontend dev server |
| `npm run build` | Production build |
| `npm run preview` | Preview production build |
| `npm run lint` | Lint with Oxlint |

---

## 📡 API Documentation

**Base URL:** `http://localhost:8000`

| Method | Endpoint | Description | Status |
|---|---|---|---|
| `GET` | `/` | Service and model info | ✅ Available |
| `GET` | `/health` | Health check | ✅ Available |
| `POST` | `/predict` | Predict heart disease risk | ✅ Available |
| `GET` | `/patients` | List patients | 🛣 Planned |
| `GET` | `/predictions` | Prediction history | 🛣 Planned |
| `GET` | `/report/{id}` | Download PDF report | 🛣 Planned |

### `POST /predict`

**Request**

```json
{
  "age": 54, "sex": 1, "cp": 0, "trestbps": 130, "chol": 246,
  "fbs": 0, "restecg": 1, "thalach": 150, "exang": 0,
  "oldpeak": 1.0, "slope": 1, "ca": 0, "thal": 2
}
```

**Response `200 OK`**

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

**cURL**

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"age":54,"sex":1,"cp":0,"trestbps":130,"chol":246,"fbs":0,"restecg":1,"thalach":150,"exang":0,"oldpeak":1.0,"slope":1,"ca":0,"thal":2}'
```

**Python**

```python
import requests

payload = {"age": 54, "sex": 1, "cp": 0, "trestbps": 130, "chol": 246,
           "fbs": 0, "restecg": 1, "thalach": 150, "exang": 0,
           "oldpeak": 1.0, "slope": 1, "ca": 0, "thal": 2}

print(requests.post("http://localhost:8000/predict", json=payload).json())
```

**Error codes**

| Code | Meaning |
|---|---|
| `422` | Invalid or out-of-range input |
| `500` | Prediction failed |
| `503` | Model not loaded |

---

## 📁 Folder Structure

```
cardioai/
├── 📂 backend/
│   ├── main.py                      # FastAPI app, schema, /predict
│   ├── heart_disease_model.pkl      # Trained Logistic Regression model
│   └── requirements.txt
│
├── 📂 frontend/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js           # Custom animations (heartbeat, blobs, shimmer)
│   ├── postcss.config.js
│   ├── .oxlintrc.json
│   └── 📂 src/
│       └── main.jsx                 # React entry point
│
├── 📂 notebooks/                    # Colab / Jupyter training notebook
├── 📂 docs/
│   └── 📂 screenshots/
├── .gitignore
└── README.md
```

---

## 🚀 Deployment Guide

### 🔹 Frontend → Vercel

1. Push the repo to GitHub.
2. Import the project in [Vercel](https://vercel.com) and set the **root directory** to `frontend`.
3. Build command: `npm run build` · Output directory: `dist`.
4. Add `VITE_API_URL` pointing to your Render backend URL.

### 🔹 Backend → Render

1. Create a new **Web Service** on [Render](https://render.com) with root directory `backend`.
2. Build command: `pip install -r requirements.txt`
3. Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. Add environment variables (`DATABASE_URL`, `ALLOWED_ORIGINS`).
5. Attach a Render **PostgreSQL** instance if using patient history.

### 🔐 Production checklist

- [ ] Restrict CORS from `*` to your Vercel domain
- [ ] Store secrets in environment variables only
- [ ] Enable HTTPS (default on Vercel and Render)
- [ ] Add rate limiting and request logging

---

## 🔮 Future Enhancements

- [ ] 🔍 SHAP / LIME explainability per prediction
- [ ] 🧑‍⚕️ Patient management with PostgreSQL + SQLAlchemy
- [ ] 🕘 Prediction history and trend tracking
- [ ] 📈 Analytics dashboard (risk distribution, cohort insights)
- [ ] 📄 PDF report generation
- [ ] 🔐 JWT authentication and role-based access (doctor / admin)
- [ ] 🤖 Model comparison (Random Forest, XGBoost, SVM) and hyperparameter tuning
- [ ] 🔄 MLOps: model versioning, CI/CD, monitoring and drift detection
- [ ] 🐳 Docker and docker-compose setup
- [ ] 🌐 Multi-language support and PWA

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the project
2. Create a branch: `git checkout -b feature/amazing-feature`
3. Commit: `git commit -m "feat: add amazing feature"`
4. Push: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 👨‍💻 Author

<div align="center">

**Your Name**
*AI/ML Engineer · Data Scientist · Full Stack Developer*

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/your-username)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/your-profile)
[![Portfolio](https://img.shields.io/badge/Portfolio-FF5722?style=for-the-badge&logo=googlechrome&logoColor=white)](https://your-portfolio.com)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:you@example.com)

</div>

---

## 📊 GitHub Stats

<div align="center">

![Stats](https://github-readme-stats.vercel.app/api?username=your-username&show_icons=true&theme=radical&hide_border=true)
![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=your-username&layout=compact&theme=radical&hide_border=true)

![Streak](https://streak-stats.demolab.com?user=your-username&theme=radical&hide_border=true)

![Repo Stars](https://img.shields.io/github/stars/your-username/cardioai?style=social)
![Forks](https://img.shields.io/github/forks/your-username/cardioai?style=social)
![Issues](https://img.shields.io/github/issues/your-username/cardioai?style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/your-username/cardioai?style=flat-square)

</div>

---

## 📜 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.

---

## 🔑 Keywords

`Machine Learning` · `Artificial Intelligence` · `Healthcare AI` · `Heart Disease Prediction` · `Predictive Modeling` · `Logistic Regression` · `Classification` · `Explainable AI` · `Data Science` · `Feature Engineering` · `scikit-learn` · `Pandas` · `NumPy` · `FastAPI` · `REST API` · `Python` · `React.js` · `Vite` · `Tailwind CSS` · `PostgreSQL` · `Full Stack Development` · `SaaS` · `Model Deployment` · `MLOps` · `Vercel` · `Render` · `Data Visualization` · `Healthcare Analytics`

<div align="center">

⭐ **If you found this project useful, please give it a star!** ⭐

Made with ❤️ and 🧠 by **Your Name**

</div>
