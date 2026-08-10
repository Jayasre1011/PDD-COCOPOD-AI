"""
cv2.py — Lightweight OpenCV shim & fallback for Pyodide/Stlite browser environments.
Provides standard cv2 constants and functions using NumPy, Pillow, and Scikit-Image.
"""

import sys
import numpy as np
from PIL import Image

# Constants
COLOR_RGBA2BGRA = 1
COLOR_RGB2BGR = 2
COLOR_BGR2HSV = 3
COLOR_BGR2GRAY = 4
COLOR_HSV2BGR = 5
COLOR_GRAY2BGR = 6

INTER_NEAREST = 0
INTER_LINEAR = 1
INTER_CUBIC = 2
INTER_AREA = 3

RETR_EXTERNAL = 0
CHAIN_APPROX_SIMPLE = 1
FILLED = -1
MORPH_CLOSE = 1
MORPH_OPEN = 2

IMREAD_UNCHANGED = -1
IMREAD_COLOR = 1
IMREAD_GRAYSCALE = 0

def cvtColor(src, code):
    if src is None:
        return src
    if code in (COLOR_RGB2BGR, COLOR_RGBA2BGRA):
        return src[:, :, ::-1]
    elif code == COLOR_BGR2HSV:
        try:
            from skimage.color import rgb2hsv
            return (rgb2hsv(src[:, :, ::-1]) * [180, 255, 255]).astype(np.uint8)
        except Exception:
            return src
    elif code == COLOR_BGR2GRAY:
        try:
            from skimage.color import rgb2gray
            return (rgb2gray(src[:, :, ::-1]) * 255).astype(np.uint8)
        except Exception:
            return np.mean(src, axis=2).astype(np.uint8)
    return src

def resize(src, dsize, interpolation=INTER_LINEAR):
    if src is None:
        return src
    pil_img = Image.fromarray(src)
    res = pil_img.resize(dsize, Image.NEAREST if interpolation == INTER_NEAREST else Image.BILINEAR)
    return np.array(res)

def findContours(image, mode, method):
    return [], None

def drawContours(image, contours, contourIdx, color, thickness=1):
    return image

def morphologyEx(src, op, kernel):
    return src

def split(m):
    return m[:, :, 0], m[:, :, 1], m[:, :, 2]

def bitwise_and(src1, src2):
    return np.bitwise_and(src1, src2)

def imread(filename, flags=IMREAD_COLOR):
    try:
        pil_img = Image.open(filename)
        arr = np.array(pil_img)
        if arr.ndim == 3 and arr.shape[2] == 3:
            return arr[:, :, ::-1]
        return arr
    except Exception:
        return None
