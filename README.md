# 🚀 Flask CI/CD Pipeline — Jenkins & Docker

A fully containerized **CI/CD pipeline** for a Flask web application, built with **Jenkins** and **Docker**. The app simulates a **Data Pipeline Monitoring Dashboard** and is automatically built, tested, and deployed through a Jenkins pipeline.

---

## 🏗️ Project Structure

```
├── app.py               # Flask application
├── test_app.py          # Pytest unit tests
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker image definition
└── Jenkinsfile          # CI/CD pipeline definition
```

---

## ⚙️ CI/CD Pipeline Stages

The Jenkins pipeline runs 4 automated stages:

| Stage | Description |
|---|---|
| **Clone** | Pulls latest code from GitHub via `checkout scm` |
| **Build** | Sets up the application environment |
| **Test** | Runs automated Pytest unit tests |
| **Deploy** | Builds & runs the Docker container |

---

## 🐳 Docker

The app runs inside a lightweight Docker container based on `python:3.9-slim`.

**Build & Run locally:**
```bash
# Build the image
docker build -t flask-cicd-app .

# Run the container
docker run -p 5000:5000 flask-cicd-app
```

Then open your browser at: `http://localhost:5000`

---

## 🧪 Testing

Unit tests written with **Pytest**:

```bash
pip install -r requirements.txt
pytest test_app.py
```

---

## 📦 Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
