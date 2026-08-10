"""
test_segmentation.py - Unit tests for image segmentation module.
"""

import pytest
import numpy as np
from src.segmentation import segment_rgb_pod, segment_thermal_pod

def test_segment_rgb_pod_4channel():
    dummy_rgba = np.random.randint(0, 256, (100, 100, 4), dtype=np.uint8)
    mask, bgr = segment_rgb_pod(dummy_rgba)
    assert mask.shape == (100, 100), f"Mask shape mismatch: {mask.shape}"
    assert bgr.shape == (100, 100, 3), f"BGR image shape mismatch: {bgr.shape}"

def test_segment_rgb_pod_3channel():
    dummy_bgr = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
    mask, bgr = segment_rgb_pod(dummy_bgr)
    assert mask.shape == (100, 100), f"Mask shape mismatch: {mask.shape}"
    assert bgr.shape == (100, 100, 3), f"BGR image shape mismatch: {bgr.shape}"

def test_segment_thermal_pod():
    dummy_thermal = np.random.randint(0, 256, (120, 160, 3), dtype=np.uint8)
    mask = segment_thermal_pod(dummy_thermal)
    assert mask.shape == (120, 160), f"Thermal mask shape mismatch: {mask.shape}"
    assert mask.dtype == np.uint8, f"Mask dtype mismatch: {mask.dtype}"
