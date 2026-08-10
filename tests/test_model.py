"""
test_model.py - Unit tests for CocoaPodAI Machine Learning models.
"""

import pytest
import numpy as np
from pathlib import Path
import joblib

MODEL_DIR = Path(__file__).resolve().parent.parent / "models"

def test_svm_single_model_integrity():
    model_path = MODEL_DIR / "svm_single.pkl"
    assert model_path.exists(), f"Model file missing: {model_path}"
    
    model = joblib.load(model_path)
    assert model is not None, "Failed to load svm_single.pkl"
    assert hasattr(model, "predict"), "Model object has no predict method"
    
def test_svm_full_model_integrity():
    model_path = MODEL_DIR / "svm_full.pkl"
    assert model_path.exists(), f"Model file missing: {model_path}"
    
    model = joblib.load(model_path)
    assert model is not None, "Failed to load svm_full.pkl"
    assert hasattr(model, "predict"), "Model object has no predict method"

def test_model_dummy_prediction():
    model_path = MODEL_DIR / "svm_single.pkl"
    model = joblib.load(model_path)
    
    # Generate dummy input matching feature vector shape
    n_features = getattr(model, "n_features_in_", 33)
    dummy_input = np.random.rand(1, n_features).astype(np.float32)
    
    pred = model.predict(dummy_input)
    assert len(pred) == 1, "Prediction output length mismatch"
    
    if hasattr(model, "predict_proba"):
        probs = model.predict_proba(dummy_input)
        assert probs.shape[0] == 1, "Probability output shape mismatch"
