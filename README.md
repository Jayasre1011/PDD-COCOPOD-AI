# 🍫 CocoaPodAI — Multimodal Cocoa Pod Classification System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/)
[![GitHub Actions CI](https://github.com/shalz-collab/cocopod-AI/actions/workflows/ci.yml/badge.svg)](https://github.com/shalz-collab/cocopod-AI/actions)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An **SVM-based multimodal image classification system** for cocoa pod ripeness assessment and disease diagnosis using fused **RGB** and **Thermal** image signatures.

---

## 🌟 Features

- 🔬 **Multimodal Classification**: Combines visible rind color (RGB/HSV) and thermal heat signatures (FLIR thermal JPEGs) to accurately classify cocoa pods into 4 distinct categories:
  - 🟢 **Unripe (UR)**: Green rind, higher thermal signature due to moisture content.
  - 🟡 **Ripe (R)**: Peak golden-orange rind, optimal sugar content for harvesting.
  - 🪵 **Overripe (OR)**: Dark brown mottle, past peak harvest condition.
  - 🩺 **Diseased / Cocoa Pod Borer (CPB)**: Thermal anomalies & lesions (diagnosed independently of ripening stage).
- 📁 **Single & Batch Processing**: Support for single pod image upload as well as batch folder automated predictions with CSV export.
- 🎨 **Tailored Visual Design System**: Modern dark-mode UI customized with custom design tokens, responsive cards, and dynamic theme elements.
- ⚡ **Streamlit Powered**: Native web app interface optimized for desktop and mobile field use.

---

## 🚀 How to Deploy on Streamlit Community Cloud

Deploying to **Streamlit Community Cloud** connects directly to your GitHub repository `https://github.com/shalz-collab/cocopod-AI` and automatically updates whenever you push code changes.

### Step 1: Push Repository to GitHub
Run the following commands in your local project directory:
```bash
git init
git add .
git commit -m "Configure CocoaPodAI for Streamlit Cloud & GitHub deployment"
git branch -M main
git remote add origin https://github.com/shalz-collab/cocopod-AI.git
git push -u origin main --force
```

### Step 2: Connect Streamlit Community Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io/) and log in with your GitHub account.
2. Click **"New app"**.
3. Fill in the deployment details:
   - **Repository**: `shalz-collab/cocopod-AI`
   - **Branch**: `main`
   - **Main file path**: `Home.py`
4. Click **"Deploy!"**.

Your app will build automatically using `requirements.txt` and generate a live URL (e.g. `https://cocopod-ai.streamlit.app`).

---

## 🌐 Deploying on GitHub Pages (Optional)

This repository includes a GitHub Actions workflow (`.github/workflows/deploy-gh-pages.yml`) powered by **Stlite** (Streamlit in WebAssembly/Pyodide).

To activate:
1. Go to your repo settings on GitHub: `https://github.com/shalz-collab/cocopod-AI/settings/pages`.
2. Under **Source**, select **GitHub Actions**.
3. Push to `main` branch. The action will build and deploy the app to `https://shalz-collab.github.io/cocopod-AI/`.

---

## 💻 Running Locally

To run the application locally on your machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/shalz-collab/cocopod-AI.git
   cd cocopod-AI
   ```

2. **Create a virtual environment & install requirements**:
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate

   pip install -r requirements.txt
   ```

3. **Launch the Streamlit app**:
   ```bash
   streamlit run Home.py
   ```

---

## 📁 Repository Structure

```
cocopod-AI/
├── .github/
│   └── workflows/
│       ├── ci.yml               # GitHub Actions CI syntax & model test workflow
│       └── deploy-gh-pages.yml  # GitHub Pages Stlite deployment workflow
├── .streamlit/
│   └── config.toml              # Streamlit theme & server configuration
├── data/                        # Training sample datasets (RGB & Thermal)
├── models/
│   ├── svm_single.pkl           # Single thermal model for quick inference
│   └── svm_full.pkl             # Dual-thermal (front+back) full model
├── pages/
│   ├── 1_🔬_Predict.py          # Prediction app interface
│   └── 2_📖_Pod_Guide.py        # Interactive class guide & details
├── src/
│   ├── feature_extraction.py    # HSV, LBP, and thermal feature extraction
│   ├── segmentation.py          # Pod mask isolation & background removal
│   └── theme.py                 # Design tokens and custom CSS styling
├── Home.py                      # Application landing page
├── README.md                    # Project documentation
└── requirements.txt             # Python dependencies
```

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for details.
