"""
Regenerates frontend/index.html (the Netlify login page) from backend/main.py, so the two never drift apart.

    python tools/build_frontend.py https://agrisense-backend-jagn.onrender.com

Only needed when you change translations or styles in main.py. Without an argument it keeps the placeholder URL.
"""
import os
import pathlib
import sys

root = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root / "backend"))
os.environ["DATABASE_URL"] = "sqlite:///:memory:"
import main  # noqa: E402

base = (sys.argv[1] if len(sys.argv) > 1 else "https://YOUR-RENDER-APP.onrender.com").rstrip("/")
page = main.auth_page("en", base=base)
note = (
    "<!--\n  NO JAVASCRIPT. This login form posts to your Render backend, which signs you in and shows the chat there.\n"
    "  ONLY EDIT NEEDED: replace https://YOUR-RENDER-APP.onrender.com (2 places) with your Render URL, then upload this file to Netlify.\n"
    "  (Or run:  python tools/build_frontend.py https://your-app.onrender.com )\n-->\n"
)
(root / "frontend" / "index.html").write_text(page.replace("<body>", note + "<body>", 1), encoding="utf-8")
print("wrote frontend/index.html ->", base)
