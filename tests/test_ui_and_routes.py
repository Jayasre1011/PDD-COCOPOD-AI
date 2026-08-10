"""
test_ui_and_routes.py - Unit tests for UI theme and page route compilation.
"""

import pytest
import py_compile
from pathlib import Path
from src.theme import get_custom_theme_css

def test_theme_css_generation():
    css = get_custom_theme_css()
    assert isinstance(css, str), "Theme CSS output must be a string"
    assert "stApp" in css or "background" in css, "Expected CSS rule markers missing"

def test_page_syntax_compilation():
    root = Path(__file__).resolve().parent.parent
    files_to_compile = [
        root / "Home.py",
        root / "pages" / "1_🔬_Predict.py",
        root / "pages" / "2_📖_Pod_Guide.py",
        root / "src" / "theme.py",
        root / "src" / "feature_extraction.py",
        root / "src" / "segmentation.py"
    ]
    
    for py_file in files_to_compile:
        assert py_file.exists(), f"File missing for compilation check: {py_file}"
        res = py_compile.compile(str(py_file))
        assert res is not None, f"Failed to compile {py_file}"
