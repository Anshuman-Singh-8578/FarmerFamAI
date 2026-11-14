"""
Shows WHY Gemini fails. Runs the same calls the website makes, one step at a time.

    cd backend
    python check_gemini.py
"""
import os
import traceback

os.environ.setdefault("DATABASE_URL", "sqlite:///:memory:")  # do not touch your real database
from dotenv import load_dotenv  # noqa: E402

load_dotenv()
import main  # noqa: E402

key = main.GEMINI_API_KEY
if not key:
    raise SystemExit("GEMINI_API_KEY is empty in backend/.env")
print(f"Key: {key[:6]}...{key[-3:]} | model: {main.GEMINI_MODEL} | guard model: {main.GUARD_MODEL}\n")


def step(title, fn):
    print(f"--- {title}")
    try:
        out = fn()
        print("   OK ->", str(out)[:300].replace("\n", " "), "\n")
        return True
    except Exception as exc:
        print(f"   FAILED -> {type(exc).__name__}: {exc}\n")
        if os.getenv("VERBOSE"):
            traceback.print_exc()
        return False


client = main._get_client()  # same client the website uses (pinned API version)
step("1. plain call (what the earlier test did)", lambda: client.models.generate_content(model=main.GEMINI_MODEL, contents="Reply with the single word: OK").text)
step("2. scope guard: farming question (expect True)", lambda: main.is_farming_question([], "How do I grow tomatoes?"))
step("3. scope guard: off-topic (expect False)", lambda: main.is_farming_question([], "Write a python script"))
step("4. website call, no tools needed", lambda: main.ask_gemini([{"role": "user", "content": "Give me two tips for growing wheat."}], None, None, "en"))
step("5. website call WITH a tool (weather)", lambda: main.ask_gemini([{"role": "user", "content": "What is the weather in Pune today?"}], None, None, "en"))
step("6. website call WITH a tool (mandi prices)", lambda: main.ask_gemini([{"role": "user", "content": "Tomato price in Delhi"}], None, None, "en"))
print("Send me the FAILED lines (no key). If everything is OK here, the problem is only on Render: check its Logs tab.")
