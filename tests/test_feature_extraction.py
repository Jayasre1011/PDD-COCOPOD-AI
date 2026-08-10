"""
test_feature_extraction.py - Unit tests for CocoaPodAI feature extraction logic.
"""

import pytest
import numpy as np
from src.feature_extraction import (
    extract_rgb_features,
    extract_hsv_features,
    extract_thermal_features,
    extract_hue_histogram_features,
    extract_lbp_features,
    extract_all_features
)

def test_extract_rgb_features():
    dummy_img = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
    feats = extract_rgb_features(dummy_img)
    assert len(feats) == 6, f"Expected 6 RGB features, got {len(feats)}"
    assert all(isinstance(f, float) for f in feats)

def test_extract_hsv_features():
    dummy_img = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
    feats = extract_hsv_features(dummy_img)
    assert len(feats) == 3, f"Expected 3 HSV features, got {len(feats)}"

def test_extract_thermal_features():
    dummy_thermal = np.random.randint(0, 256, (120, 160, 3), dtype=np.uint8)
    feats = extract_thermal_features(dummy_thermal)
    assert len(feats) == 4, f"Expected 4 Thermal features, got {len(feats)}"

def test_extract_hue_histogram_features():
    dummy_img = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
    feats = extract_hue_histogram_features(dummy_img, bins=10)
    assert len(feats) == 10, f"Expected 10 Hue Histogram features, got {len(feats)}"

def test_extract_lbp_features():
    dummy_img = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
    feats = extract_lbp_features(dummy_img, n_points=8, radius=1, bins=10)
    assert len(feats) == 10, f"Expected 10 LBP features, got {len(feats)}"

def test_extract_all_features():
    rgb_img = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
    t_front = np.random.randint(0, 256, (120, 160, 3), dtype=np.uint8)
    t_back = np.random.randint(0, 256, (120, 160, 3), dtype=np.uint8)
    
    vector = extract_all_features(rgb_img, t_front, t_back)
    assert isinstance(vector, np.ndarray), "Returned vector is not a numpy array"
    assert vector.dtype == np.float32, f"Expected float32 dtype, got {vector.dtype}"
    assert vector.shape[0] == 37, f"Expected total feature dimension 37, got {vector.shape[0]}"
