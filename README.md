# Agri Sense – AI farming assistant (Gemini, login, saved chats, 10 languages)

```
backend/main.py                   <- the entire backend (FastAPI + Google GenAI + database), deploy on Render
backend/test_scope.py             <- LIVE test: does it refuse non-farming questions? (run it once with your key)
backend/legacy_reference_data.py  <- old tips/canned replies, imported by nothing (delete if unwanted)
frontend/index.html               <- the login page (HTML + CSS only, NO JavaScript), upload to Netlify
tools/build_frontend.py           <- optional: regenerates index.html from main.py (translations/styles live there)
```

## How it works (no JavaScript anywhere)
1. **Netlify page** = login/sign-up form. It posts to your Render backend.
2. Backend checks the password (scrypt hash), sets a secure cookie, and redirects you to **/app on the backend**. From then on you are on the Render address (first-party cookie, so login works in every browser).
3. **/app** shows your saved chats (sidebar), the conversation, a language picker, and your city. Every message is saved to the database, and a redirect after each send means refreshing never re-sends it.
4. **Scope control, two layers:** (1) a tiny YES/NO classifier call blocks non-farming messages and replies with a fixed refusal in the user's language; (2) the assistant's own system prompt refuses anything that slips through. If the classifier is down, layer 2 still protects.
5. **Languages:** English, हिन्दी, বাংলা, मराठी, தமிழ், తెలుగు, ગુજરાતી, ಕನ್ನಡ, മലയാളം, ਪੰਜਾਬੀ. The login page switches language with pure CSS; the app uses the language saved on your account (change it from the dropdown, it applies on your next message). Replies follow the language you type in, falling back to your chosen language.

## 1) Test the Gemini scope restriction (do this first)
```bash
cd backend
python -m venv .venv && source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
# edit backend/.env  ->  GEMINI_API_KEY=your_key
python test_scope.py
```
It runs 16 off-topic prompts (code, trivia, politics, jailbreaks, Hindi/Tamil off-topic…) and 12 farming prompts through each layer and prints BLOCKED / LEAKED / WRONGLY BLOCKED. Read the "layer 2" replies yourself; they should be short refusals. If something leaks, tell me the prompt and I will tighten the rules.

## 2) Run locally
```bash
uvicorn main:app --reload --port 8000     # open http://localhost:8000
```
With `DATABASE_URL` empty, accounts and chats go into a local file `backend/agrisense.db`.

## 3) Deploy
1. **Free Postgres** (needed because Render's free disk is erased on every restart): create a project on **neon.tech** or **supabase.com** and copy the connection string (`postgresql://…`).
2. **Render** – Blueprint from this repo (`render.yaml`) or Web Service: root dir `backend`, build `pip install -r requirements.txt`, start `uvicorn main:app --host 0.0.0.0 --port $PORT`. Env vars: `GEMINI_API_KEY`, `OPENWEATHER_API_KEY`, `DATA_GOV_API_KEY`, `DATABASE_URL`. Copy your Render URL.
3. **Frontend** – run `python tools/build_frontend.py https://your-app.onrender.com` (or edit the two placeholders in `frontend/index.html` by hand), then upload `index.html` to Netlify.
4. Optional: set `FRONTEND_URL` on Render to your Netlify URL so the backend's home page redirects there.
5. Check `https://<render-url>/api/health` (`gemini_configured: true`, `database: postgres`), then create an account from your Netlify page.

## Security built in
scrypt password hashes; random server-side sessions (HttpOnly, SameSite=Lax, Secure on https, 30 days); login brute-force limits (per IP and per email); sign-up limit; per-user message rate limit; Origin check on every POST (CSRF); users can only open/delete their own chats; all text HTML-escaped; strict CSP (no scripts, same-site forms); `Cache-Control: no-store`; API docs disabled; size caps on messages, photos, chats. Also set a spending cap on your Gemini key in Google AI Studio / Cloud.

## Known limits
- **No email verification and no "forgot password"** (both need an email-sending service). Tell me if you want them.
- Photos are analysed but **not stored**; the chat only keeps a "📷 photo attached" tag.
- Chats are stored in plain text in your database. The login page says so; mention it in your privacy notice.
- Translations were written by an AI; ask a native speaker of each language to review them (they live in `_RAW` / `TOPICS` in `main.py`).
- The "Choose file / No file chosen" text is drawn by the browser in the phone's own language; it cannot be changed without JavaScript.
- The login page's language switch needs a 2023+ browser (`:has()`); older ones show English, and the language dropdown still sets the account language at sign-up.
- Returning users keep the language saved on their account (the dropdown on the login page only matters at sign-up).
- First request after Render's free tier sleeps takes ~1 minute (a free uptime pinger on `/api/health` avoids it).
