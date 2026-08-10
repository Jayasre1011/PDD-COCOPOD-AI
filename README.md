# 🍫 CocoaPodAI — Multimodal Cocoa Pod Classification System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/)
[![GitHub Actions CI](https://github.com/Jayasre1011/-CocoaPodAI/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/Jayasre1011/-CocoaPodAI/actions)
[![Firebase Hosting](https://img.shields.io/badge/Firebase-Hosting-FFCA28?logo=firebase&logoColor=black)](https://firebase.google.com/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)

An **SVM-based multimodal image classification system** for cocoa pod ripeness assessment and disease diagnosis using fused **RGB** and **Thermal** image signatures.

---

## 🧪 Test Automation & CI/CD Pipeline

This repository features an automated 5-suite parallel test automation pipeline:
1. **Selenium - Website Tests (300)**: UI automation and page route validation.
2. **Appium - Android Tests (300)**: Mobile viewport and touch interaction checks.
3. **Validation Tests (300)**: Machine learning SVM model integrity and feature extraction verification.
4. **Deployment Status (300)**: Server health and environment sanity testing.
5. **Load Testing - Performance (300)**: Latency, memory, and concurrency benchmark suite.

All 5 test suites run concurrently and feed into **Compile Master Report & Deploy**, which compiles full JSON/CSV sheets and deploys live to **GitHub Pages**.

---

## 🌐 Deploying on GitHub Pages

This repository is configured for automatic deployment to **GitHub Pages** via `.github/workflows/ci-cd.yml` powered by **Stlite (Streamlit WebAssembly)**.
1. Enable GitHub Pages in your repository settings: **Settings** -> **Pages** -> **Source: GitHub Actions**.
2. Push your changes to `main` or trigger the workflow manually.
3. Your app will be live at `https://jayasre1011.github.io/-CocoaPodAI/`!

---

## 🔥 How to Deploy to Firebase Hosting

This repository is configured for direct deployment to **Firebase Hosting** via Firebase CLI or GitHub Actions.

### Method 1: Deploy using Firebase CLI (Command Line)

1. **Log in to Firebase**:
   ```bash
   npx -y firebase-tools login
   ```

2. **Build the static site distribution**:
   ```bash
   python scripts/build_firebase.py
   ```

3. **Deploy to Firebase Hosting**:
   ```bash
   npx -y firebase-tools deploy
   ```

Your app will be live on `https://cocopod-ai.web.app` / `https://cocopod-ai.firebaseapp.com`!

---

### Method 2: Deploy automatically via GitHub Actions

This repository includes `.github/workflows/firebase-hosting-deploy.yml`. 
To enable automatic deployment on every `git push`:
1. In your Firebase Console, go to **Project Settings** -> **Service accounts** -> **Generate new private key**.
2. Go to your GitHub repo settings (`https://github.com/Jayasre1011/-CocoaPodAI/settings/secrets/actions`).
3. Add a new secret named `FIREBASE_SERVICE_ACCOUNT_COCOPOD_AI` with the contents of the generated JSON service account key.

---

## 🚀 How to Deploy on Streamlit Community Cloud

1. Push your repository to GitHub: `https://github.com/Jayasre1011/-CocoaPodAI`
2. Go to [share.streamlit.io](https://share.streamlit.io/) and log in with GitHub.
3. Click **"New app"**, select `Jayasre1011/-CocoaPodAI`, set main file path to `Home.py`, and click **"Deploy!"**.

---

## 💻 Running Locally

```bash
python -m venv .venv
# Activate virtual environment
pip install -r requirements.txt
streamlit run Home.py
```

---

## 📄 License

Distributed under the MIT License.
