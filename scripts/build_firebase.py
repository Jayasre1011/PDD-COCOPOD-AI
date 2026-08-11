"""
build_firebase.py
Prepares static distribution directory `public/` for Firebase Hosting deployment with Stlite WebAssembly and Firebase SDK initialization.
"""

import shutil
from pathlib import Path

def main():
    root = Path(__file__).resolve().parent.parent
    public_dir = root / "public"
    
    if public_dir.exists():
        shutil.rmtree(public_dir)
        
    public_dir.mkdir(parents=True, exist_ok=True)
    
    # 1. Copy app files to public/
    shutil.copy(root / "Home.py", public_dir / "Home.py")
    shutil.copy(root / "cv2.py", public_dir / "cv2.py")
    
    (public_dir / "pages").mkdir(exist_ok=True)
    for p_file in (root / "pages").glob("*.py"):
        shutil.copy(p_file, public_dir / "pages" / p_file.name)
        
    (public_dir / "src").mkdir(exist_ok=True)
    for s_file in (root / "src").glob("*.py"):
        shutil.copy(s_file, public_dir / "src" / s_file.name)
        
    (public_dir / "models").mkdir(exist_ok=True)
    for m_file in (root / "models").glob("*.pkl"):
        shutil.copy(m_file, public_dir / "models" / m_file.name)
        
    # 2. Write Stlite index.html with Firebase SDK Analytics Config
    html_content = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>CocoaPodAI — Let's Cocoa</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@stlite/mountable@0.58.0/build/stlite.css" />
    <style>
      body { background-color: #17100B; margin: 0; }
    </style>
    <!-- Firebase SDK Config -->
    <script type="module">
      import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
      import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-analytics.js";
      
      const firebaseConfig = {
        apiKey: "AIzaSyCoJ8jkUYYdrnIVkG4_oE-z5LQjUI8WOfk",
        authDomain: "cocopod-ai.firebaseapp.com",
        projectId: "cocopod-ai",
        storageBucket: "cocopod-ai.firebasestorage.app",
        messagingSenderId: "624424104495",
        appId: "1:624424104495:web:835c0a50bbed3a8dd7ccda",
        measurementId: "G-GP3WPDREWL"
      };

      const app = initializeApp(firebaseConfig);
      const analytics = getAnalytics(app);
    </script>
  </head>
  <body>
    <div id="root"></div>
    <script src="https://cdn.jsdelivr.net/npm/@stlite/mountable@0.58.0/build/stlite.js"></script>
    <script>
      stlite.mount({
        entrypoint: "Home.py",
        files: {
          "Home.py": { url: "./Home.py" },
          "cv2.py": { url: "./cv2.py" },
          "pages/1_🔬_Predict.py": { url: "./pages/1_%F0%9F%94%AC_Predict.py" },
          "pages/2_📖_Pod_Guide.py": { url: "./pages/2_%F0%9F%93%96_Pod_Guide.py" },
          "pages/3_📊_Test_Reports.py": { url: "./pages/3_%F0%9F%93%8A_Test_Reports.py" },
          "src/theme.py": { url: "./src/theme.py" },
          "src/feature_extraction.py": { url: "./src/feature_extraction.py" },
          "src/segmentation.py": { url: "./src/segmentation.py" },
          "models/svm_single.pkl": { url: "./models/svm_single.pkl" }
        },
        requirements: [
          "numpy",
          "Pillow",
          "joblib",
          "scikit-learn",
          "scikit-image",
          "pandas"
        ]
      }, document.getElementById("root"));
    </script>
  </body>
</html>
"""
    (public_dir / "index.html").write_text(html_content, encoding="utf-8")
    print(f"✨ Successfully built Firebase public distribution directory at {public_dir}")

if __name__ == "__main__":
    main()
