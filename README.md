# 🧠 Predicting Human Talent Churn — End-to-End MLOps Project

This project delivers a complete MLOps pipeline to predict employee attrition using open-source tools and cloud-native patterns. It integrates automation, model monitoring, and deployment best practices.

## 🚀 Objective

Design and deploy a scalable and reproducible machine learning system to:
- Predict whether an employee is at risk of leaving the company.
- Automatically retrain and monitor model performance over time.
- Enable actionable insights for HR decision-making.

---

## 🛠️ Tech Stack

| Layer | Tools / Frameworks |
|-------|--------------------|
| **ML & Training** | Scikit-learn, XGBoost, RandomForest |
| **MLOps Framework** | ZenML |
| **Model Serving** | BentoML |
| **Experiment Tracking** | Comet ML |
| **Drift Monitoring** | Evidently |
| **CI/CD & Automation** | GitHub Actions |
| **Data & Artifacts Storage** | MinIO |
| **Infrastructure** | Docker, Docker Compose |

---

## 📁 Project Structure

```bash
.
├── .github/workflows/       # CI/CD workflows for GitHub Actions
├── bentoml/                 # BentoML service and artifact definitions
├── data/                    # Input data and datasets
├── docker/                  # Docker configuration and helper scripts
├── github_runner/           # GitHub self-hosted runner setup
├── notebooks/               # EDA and experimental notebooks
├── trainer/                 # Model training and evaluation scripts
├── .env                     # Environment variables (not versioned)
├── .gitignore               # Git ignore rules
├── .infisical.json          # Infisical secret manager config
├── .python-version          # Python version for the project
├── LICENSE                  # Project license (MIT)
├── README.md                # Project documentation
├── Taskfile.yaml            # Task runner automation config
├── docker-compose.yaml      # Docker Compose orchestration
├── pyproject.toml           # Project and dependency configuration
└── uv.lock                  # Dependency lock file for uv
```

---

## 🔄 Pipeline Overview

1. **Preprocessing** – Clean and transform HR data.
2. **Trainer** – Train multiple models and log metrics to Comet ML.
3. **Evaluator** – Compare models and select the best candidate.
4. **Model Registry** – Save model and metadata to MinIO.
5. **Deployment** – Serve model with BentoML as a REST API.
6. **Monitoring** – Track drift using Evidently.
7. **CI/CD** – Automated retraining and deployment triggered via GitHub Actions and act.

---

## 📊 Dataset

- Dataset: [IBM HR Analytics Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
- Features include job satisfaction, salary, distance from home, and other employee-related variables.

---

## 📈 Model Performance

- Evaluated models: Logistic Regression, Random Forest, XGBoost
- Tracked metrics: Accuracy, F1 Score
- Best model selected based on F1 Score

---

## 💡 Business Impact

> **"Enabled proactive talent retention by combining predictive modeling with automated monitoring and drift detection."**

This solution allows HR teams to act early on attrition risk by integrating real-time predictions and monitoring pipelines.

---

## 📋 To-Do / Roadmap

- [ ] Integrate model retraining on drift detection
- [ ] Add role-based access and secret management (Infisical)
- [ ] Deploy full stack with Docker Compose
- [ ] Enable monitoring dashboard with Grafana/Prometheus

---

## 📎 References

- [ZenML Documentation](https://docs.zenml.io/)
- [BentoML Documentation](https://docs.bentoml.com/)
- [Comet ML](https://www.comet.com/)
- [Evidently AI](https://evidentlyai.com/)

---

## 📬 Contact

**Jefferson A. Areche R.**  
📧 [LinkedIn](https://www.linkedin.com/in/jefferson-angel-areche-rojas-5b0a65132) | 🧑‍💻 [GitHub](https://github.com/jeffangel/)