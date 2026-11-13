"""
Shows WHY Gemini is failing and which models your key can use.

    cd backend
    python check_gemini.py
"""
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()
key = os.getenv("GEMINI_API_KEY", "").strip()
model = os.getenv("GEMINI_MODEL", "").strip() or "gemini-3.5-flash-lite"
if not key:
    raise SystemExit("GEMINI_API_KEY is empty in backend/.env")

client = genai.Client(api_key=key)
print(f"Key: {key[:6]}...{key[-3:]}   Model to test: {model}\n")

print("Models available to this key (flash family):")
try:
    names = sorted(m.name.replace("models/", "") for m in client.models.list() if "flash" in m.name)
    print("  " + "\n  ".join(names) if names else "  (none found)")
except Exception as exc:
    print("  Could not list models ->", exc)

print(f"\nTest call to {model}:")
try:
    r = client.models.generate_content(model=model, contents="Reply with the single word: OK")
    print("  SUCCESS ->", (r.text or "").strip()[:80])
except Exception as exc:
    print("  FAILED  ->", exc)
    print("\n  Typical meanings:  API_KEY_INVALID = wrong/disabled key | 404 'not found' = model name not available to you"
          " | 403 PERMISSION_DENIED = key restricted or API not enabled | 429 = quota")
