# ROADMAP.md — Luminary AI — Run-First Restructuring Roadmap

> **Goal order (do not skip ahead):**
> **Phase 0 — get the current project running locally end-to-end** → then 1) make it safe &
> correct → 2) reliable → 3) data/intelligence → 4) production-grade → 5) polish & differentiate.
>
> **Full repo context:** [CLAUDE.md](CLAUDE.md). Verified against source on **2026-06-21**.
>
> **Format of every item:**
> - **Issue** — what's wrong (concise).
> - **How we'll solve it** — detailed, executable steps (files, commands, code, acceptance). Written
>   so you *or* an AI (e.g. Claude Code) can pick up a single item and finish it without extra context.
> - **Impact** — what it buys us (concise).
>
> **Legend** — Effort: **S** (<½ day) · **M** (1–3 days) · **L** (1+ week). Priority: **P0** blocks
> running · **P1** critical · **P2** important · **P3** nice-to-have.
>
> **How to execute an item with an AI:** paste `CLAUDE.md` + the one item's "How we'll solve it"
> block, and say "do this, then show me the diff and how to verify."

---

# PHASE 0 — GET IT RUNNING LOCALLY  *(the immediate goal)*

> Target end state: `uvicorn server:app` serves the API on `:8000`, `npm run dev` serves the UI on
> `:3000`, the UI calls **your local** backend, and every feature returns a real response.

## 0.1 Backend install is non-reproducible and may fail outright  `Effort: S · P0`
**Issue:** `ml/requirements.txt` is fully unpinned, lists `langchain-pinecone` twice, and the code
uses a deprecated import (`from langchain.embeddings import HuggingFaceEmbeddings` in
`ml/chat/src/helper.py`) that newer LangChain removed — so a fresh `pip install` can pull
incompatible versions and the app can crash on import.

**How we'll solve it:**
1. Create a clean venv and install the *current* loose set once to discover a working combination:
   ```bash
   cd ml
   python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. If the chatbot import fails, switch to the maintained package:
   ```bash
   pip install langchain-huggingface
   ```
   Then edit `ml/chat/src/helper.py`:
   ```python
   # before
   from langchain.embeddings import HuggingFaceEmbeddings
   # after
   from langchain_huggingface import HuggingFaceEmbeddings
   ```
3. Once the server boots and a request succeeds, **freeze** the exact working versions and dedupe:
   ```bash
   pip freeze > requirements.lock.txt
   ```
   Rewrite `ml/requirements.txt` to pin every direct dependency with `==` (copy versions from the
   lockfile), remove the duplicate `langchain-pinecone`, and add `langchain-huggingface==<ver>`.
   Keep only what's imported (drop `pandas`, `pypdf`, `langchain-openai`, `langchain-experimental`
   if `grep -rn "import pandas\|pypdf\|langchain_openai\|langchain_experimental" ml/` is empty).
4. Acceptance: delete the venv, recreate it, `pip install -r requirements.txt`, and the server
   starts with no import errors.

**Impact:** Reproducible installs; the #1 silent reason "it runs on my machine but not on a clean clone / Render" disappears.

## 0.2 Backend needs valid API keys (and the old ones are compromised)  `Effort: S · P0`
**Issue:** The backend needs `GROQ_API_KEY`, `PINECONE_API_KEY`, `HUGGINGFACEHUB_API_TOKEN` in
`ml/.env`. The previously committed keys leaked into git history and must not be reused.

**How we'll solve it:**
1. Generate **fresh** keys: Groq (`console.groq.com/keys`), Pinecone (`app.pinecone.io`),
   HuggingFace (`huggingface.co/settings/tokens`, read scope is enough for model download).
2. Create `ml/.env` (already git-ignored):
   ```env
   GROQ_API_KEY=gsk_...
   PINECONE_API_KEY=pcsk_...
   HUGGINGFACEHUB_API_TOKEN=hf_...
   # OPENAI_API_KEY / REPLICATE_API_TOKEN: leave out — not used by current code
   ```
3. Sanity check they load: `cd ml && python -c "import config; print(bool(config.GROQ_API_KEY))"`
   should print `True`.
4. (Full rotation/history scrub of the *old* keys is **Phase 1.1** — for running locally, new keys are enough.)

**Impact:** The LLM features (company lookup, SWOT, taglines, SEO) can return real data locally.

## 0.3 Run the backend with the correct entrypoint  `Effort: S · P0`
**Issue:** README says `uvicorn main:app`, but there is no `main.py`; the app lives in `server.py`.

**How we'll solve it:**
1. Run:
   ```bash
   cd ml && source venv/bin/activate
   uvicorn server:app --host 0.0.0.0 --port 8000 --reload
   ```
2. Verify: open `http://localhost:8000/docs` (Swagger) and `GET http://localhost:8000/api/home`
   returns the hello/team JSON.
3. Fix the README now so nobody hits this again (`README.md:55`: `main:app` → `server:app`).

**Impact:** Backend boots first try; onboarding stops failing at step one.

## 0.4 Frontend environment config  `Effort: S · P0`
**Issue:** The frontend needs Firebase + SMTP env vars (and an API base URL) that aren't documented in one place; without them, auth/contact break and the build warns.

**How we'll solve it:**
1. Create `frontend/.env.local` (git-ignored):
   ```env
   NEXT_PUBLIC_FIREBASE_API_KEY=...
   NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=...
   NEXT_PUBLIC_FIREBASE_PROJECT_ID=...
   NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=...
   NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=...
   NEXT_PUBLIC_FIREBASE_APP_ID=...
   SMTP_EMAIL=your@gmail.com          # Gmail address for the contact form
   SMTP_PASSWORD=your_gmail_app_password   # 16-char Gmail "App Password", not your login
   NEXT_PUBLIC_API_URL=http://localhost:8000   # used by 0.5
   ```
2. Get Firebase values from Firebase Console → Project settings → "Your apps" → SDK config.
3. Get the Gmail App Password from Google Account → Security → 2-Step Verification → App passwords.
4. Install + run:
   ```bash
   cd frontend && npm install && npm run dev
   ```
5. Acceptance: `http://localhost:3000` loads with no red console errors about missing Firebase config.

**Impact:** Auth pages, contact email, and API calls all have the config they need to function.

## 0.5 Point the frontend at YOUR local backend (centralize the URL)  `Effort: S · P0`
**Issue:** `https://dotslash-backend.onrender.com` is hardcoded in 5 components, so `npm run dev`
always hits the (cold-starting, possibly dead) Render box instead of your local backend. Exact sites:
`Analysis.tsx:132`, `Chatbot.tsx:256`, `ChatbotSmall.tsx:109`, `CompanyInput.tsx:72`,
`StartForm.tsx:53` (which defines its own `const API_BASE_URL`).

**How we'll solve it:**
1. Create one source of truth:
   ```ts
   // frontend/src/lib/api.ts
   export const API_BASE_URL =
     process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";
   ```
2. In each of the 5 files, import it and replace the literal:
   ```ts
   import { API_BASE_URL } from "@/lib/api";
   // fetch(`${API_BASE_URL}/company?company=...`)  etc.
   ```
   In `StartForm.tsx`, delete the local `const API_BASE_URL = '...'` (line 53) and import the shared one.
3. Confirm none remain: `grep -rn "dotslash-backend.onrender.com" frontend/src` → no results.
4. Acceptance: with the backend running and `NEXT_PUBLIC_API_URL=http://localhost:8000`, a company
   search in the UI shows the request hitting `localhost:8000` in the Network tab.

**Impact:** Local dev actually exercises local code; switching environments (local/staging/Render) is one env var, not a code edit.

## 0.6 Make CORS accept your local frontend  `Effort: S · P0`
**Issue:** `server.py` sets `allow_origins=["*"]` **with** `allow_credentials=True` — an invalid
combination the browser rejects, so any credentialed request from `:3000` can be blocked.

**How we'll solve it (minimal version to unblock dev; full lockdown is 1.2):**
```python
# ml/server.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
```
Acceptance: a POST from the UI to `/companies-analysis` succeeds with no CORS error in the console.

**Impact:** Browser ↔ backend calls work reliably in local dev.

## 0.7 Make the RAG chatbots actually answer  `Effort: S–M · P0 (only if chatbots are in scope now)`
**Issue:** `/medical-bot` and `/marketing-bot` read from pre-existing Pinecone indexes `chatbot1`
and `chatbot2`. If those indexes don't exist in your new Pinecone project (new key from 0.2), the
chatbots return errors or empty answers. The PDFs/data that built them are **not** in the repo.

**How we'll solve it — pick the path that matches your situation:**
- **Path A — you still have the original indexes:** point `PINECONE_API_KEY` at the project that
  contains `chatbot1`/`chatbot2`. Confirm with the Pinecone console that both exist and have
  vectors. Done — chatbots work as-is.
- **Path B — you need to (re)create them:** write a one-off ingestion script (this is the seed of
  the reproducible pipeline in **3.4**):
  ```python
  # ml/chat/ingest.py
  import os
  from dotenv import load_dotenv
  from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
  from langchain.text_splitter import RecursiveCharacterTextSplitter
  from langchain_pinecone import PineconeVectorStore
  from pinecone import Pinecone, ServerlessSpec
  from chat.src.helper import download_hugging_face_embeddings

  load_dotenv()
  INDEX = "chatbot1"          # run again with "chatbot2" for marketing
  DATA_DIR = "ml/chat/data"   # put your source PDFs here

  pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
  if INDEX not in [i["name"] for i in pc.list_indexes()]:
      pc.create_index(INDEX, dimension=384, metric="cosine",
                      spec=ServerlessSpec(cloud="aws", region="us-east-1"))

  docs = DirectoryLoader(DATA_DIR, glob="*.pdf", loader_cls=PyPDFLoader).load()
  chunks = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50).split_documents(docs)
  PineconeVectorStore.from_documents(chunks, download_hugging_face_embeddings(), index_name=INDEX)
  print(f"Ingested {len(chunks)} chunks into {INDEX}")
  ```
  Run: `cd ml && python -m chat.ingest`. (Embedding dim must be **384** to match `all-MiniLM-L6-v2`.)
- **Path C — defer chatbots:** if you only want the LLM features running today, skip this; the four
  Groq features (0.2) work without Pinecone. Mark chatbots "Coming soon" in the UI.

**Impact:** Chatbots return grounded answers locally — or you consciously defer them without blocking the rest of the app.

## 0.8 Smoke-test every feature (Phase 0 Definition of Done)  `Effort: S · P0`
**Issue:** "It starts" ≠ "it works." Need a fast, repeatable check that each feature returns real data.

**How we'll solve it — run through this checklist once both servers are up:**
- [ ] `GET /api/home` → 200 JSON.
- [ ] **Explore**: enter a company + location → company + 5 competitors render (`/company`).
- [ ] **SWOT**: click View SWOT → 3 SWOT cards render (`/companies-analysis`).
- [ ] **Build**: submit description + sector → 5 names+taglines and SEO keywords render
      (`/tagline-generator`, `/seo`).
- [ ] **Chat** (if 0.7 done): send a message → grounded reply renders (`/medical-bot`).
- [ ] **Marketing widget** (if 0.7 done): floating bot replies (`/marketing-bot`).
- [ ] **Contact**: submit the form → email arrives (`sendMail`).
- [ ] Network tab shows all calls hitting `localhost:8000`.

**Impact:** A green checklist = the project genuinely runs end-to-end; this becomes your manual regression test until automated tests land (4.1).

---

# PHASE 1 — SECURITY & CORRECTNESS  *(before any public/shared exposure)*

## 1.1 Leaked API keys still live in git history  `Effort: S · P1 🔴`
**Issue:** `ml/.env` with real keys was committed (`a5382e8`, `3eba29d`). It's gone from the working
tree but recoverable from history — assume all old keys are compromised.

**How we'll solve it (destructive — run yourself, coordinate with anyone who has a clone):**
1. **Rotate every old key** in each provider dashboard (Groq, Pinecone, HuggingFace, and OpenAI/Replicate if those keys were ever real). This is the only step that actually stops abuse.
2. Scrub the file from all history:
   ```bash
   pip install git-filter-repo
   git filter-repo --path ml/.env --invert-paths
   git push --force --all && git push --force --tags
   ```
   (Or use BFG Repo-Cleaner.) Note: this rewrites every commit hash.
3. Confirm: `git log --all --oneline -- ml/.env` returns nothing.

**Impact:** Closes an active financial/security exposure; clean history for a public/portfolio repo.

## 1.2 CORS is wide open  `Effort: S · P1 🟠`
**Issue:** Beyond the dev fix in 0.6, production must not accept all origins.

**How we'll solve it:** make the allow-list env-driven so local/staging/prod differ by config only:
```python
# ml/server.py
import os
origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")
app.add_middleware(CORSMiddleware,
    allow_origins=origins, allow_credentials=True,
    allow_methods=["GET", "POST"], allow_headers=["*"])
```
Set `ALLOWED_ORIGINS=https://<your-vercel-domain>` on Render. Acceptance: requests from the Vercel
domain succeed; requests from a random origin are blocked.

**Impact:** Prevents arbitrary sites from driving your paid backend from a user's browser.

## 1.3 No `.env.example` for onboarding  `Effort: S · P2`
**Issue:** New devs (and future-you) don't know which env vars exist without reading code.

**How we'll solve it:** commit `ml/.env.example` and `frontend/.env.example` containing every key
from §0.2/§0.4 with **empty** values and a one-line comment each. Reference them in the README.

**Impact:** Frictionless setup; no more "which vars do I need?"

## 1.4 Bare `except` leaks internal errors  `Effort: S · P2 🟡`
**Issue:** `/company` (`server.py:40-43`) catches everything and returns `{"error": str(e)}` with
HTTP 200 — leaks internals and lies about success.

**How we'll solve it:**
```python
import logging
log = logging.getLogger("luminary")

@app.get("/company")
def get_company_details(company: str, location: str):
    try:
        ...
        return company_info
    except HTTPException:
        raise
    except Exception:
        log.exception("get_company_details failed")
        raise HTTPException(status_code=502, detail="Failed to fetch company info")
```
Match the pattern `/companies-analysis` already uses (raise `HTTPException`). Acceptance: a forced
failure returns a non-200 status with a generic message; the stack trace appears in server logs only.

**Impact:** No information leakage; clients get correct status codes; easier debugging via logs.

## 1.5 Fragile LLM JSON parsing  `Effort: M · P2 🟡`
**Issue:** `companies.py` and `analysis.py` regex-strip ```` ```json ```` fences then `json.loads`,
which throws on any malformed model output → 500s.

**How we'll solve it:**
1. Ask Groq for strict JSON: pass `response_format={"type": "json_object"}` in the chat completion call.
2. Define Pydantic models for the expected shapes (e.g. `Company`, `CompetitorList`, `SwotList`) and
   parse with `Model.model_validate_json(raw)`.
3. Wrap in a retry-once-then-fallback: on `ValidationError`, retry the call once with a "return only
   valid JSON" reminder; if it still fails, return a structured error, not a crash.

**Impact:** Far fewer 5xx from the core features; predictable, typed responses the frontend can trust.

---

# PHASE 2 — RELIABILITY & CORE UX

## 2.1 RAG re-initializes on every request  `Effort: S · P1 🟡`
**Issue:** `chat_service.get_response()` calls `load_dotenv()`, downloads the embedding model, and
re-opens the Pinecone index on **every** message (see `ml/services/chat_service.py:12-41`) — adds
seconds and memory churn per call. Same in `marketing_chatbot_service.py`.

**How we'll solve it:** build the heavy objects once at startup and reuse them.
```python
# ml/server.py
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    from chat.src.helper import download_hugging_face_embeddings
    app.state.embeddings = download_hugging_face_embeddings()   # load model ONCE
    yield

app = FastAPI(lifespan=lifespan)
```
Refactor `chat_service` to accept the shared `embeddings` (and a cached retriever/chain per index)
instead of rebuilding them. Keep `from_existing_index` results cached in a module-level dict keyed by
index name. Acceptance: second chatbot request is markedly faster than the first; embeddings load
appears once in logs.

**Impact:** Chatbot latency drops to mostly the Groq round-trip; lower memory thrash; fewer cold-path bugs.

## 2.2 No auth on paid LLM endpoints  `Effort: M · P1 🟠`
**Issue:** Every AI route is publicly callable; each call spends Groq/Pinecone quota. Firebase login
is cosmetic — the backend verifies nothing.

**How we'll solve it:**
1. `pip install firebase-admin`; initialize with a service-account JSON (store path in env, file
   git-ignored).
2. Add a dependency that verifies the Firebase ID token:
   ```python
   # ml/auth.py
   from fastapi import Depends, HTTPException, Header
   from firebase_admin import auth, credentials, initialize_app
   initialize_app(credentials.Certificate(os.environ["FIREBASE_CREDENTIALS"]))

   def require_user(authorization: str = Header(...)):
       try:
           return auth.verify_id_token(authorization.removeprefix("Bearer "))
       except Exception:
           raise HTTPException(401, "Invalid or missing auth token")
   ```
3. Add `user = Depends(require_user)` to each AI route (or `router.dependencies=[...]`).
4. Frontend: send `Authorization: Bearer ${await user.getIdToken()}` on every API call (add it in
   `lib/api.ts`'s fetch wrapper).

**Impact:** Only logged-in users can spend your quota; abuse and surprise bills drop sharply.

## 2.3 Rate limiting + input length caps  `Effort: M · P1 🟠`
**Issue:** No throttle and no max input — a script (or a 100k-char chatbot message) can run up Groq cost.

**How we'll solve it:**
1. `pip install slowapi`; attach a limiter keyed by user id / IP, e.g. `@limiter.limit("20/minute")`
   on AI routes.
2. Enforce input size with Pydantic: `msg: constr(max_length=2000)` on chatbot bodies; reject
   oversized query params with a 422.

**Impact:** Predictable cost ceiling; resilience against abuse and accidental loops.

## 2.4 `/dashboard` 404 + no route guards  `Effort: M · P1`
**Issue:** Successful login redirects to `/dashboard`, which doesn't exist → users hit a 404. No page
is access-controlled.

**How we'll solve it:**
1. Create `frontend/src/app/dashboard/page.tsx` — a minimal authed landing (greeting + links to
   Explore/Build/Chat).
2. Add a client guard hook used by protected pages:
   ```tsx
   // redirect to /signin if no Firebase user
   useEffect(() => onAuthStateChanged(auth, u => { if (!u) router.replace("/signin"); }), []);
   ```
   (Or a `(protected)` route group with a shared layout that runs the check once.)
3. Optionally gate at the edge with `middleware.ts` checking a session cookie for SSR-safe protection.

**Impact:** Login leads somewhere real; protected areas actually require auth — the core flow stops being broken.

## 2.5 Render cold-start looks like a crash  `Effort: S · P2`
**Issue:** The free Render backend sleeps; the first request can take 2–5 min with no UI feedback, so
users see a hang/timeout.

**How we'll solve it:**
1. Add a fetch wrapper with timeout + retry/backoff in `lib/api.ts`; on slow/failed first call show a
   "Waking the server up, this can take a minute…" banner.
2. Optionally ping `/health` on app load to trigger the wake early, and/or add an external cron
   (e.g. cron-job.org) hitting `/health` every ~10 min to keep it warm.

**Impact:** Demos and first impressions stop failing silently; perceived reliability jumps.

## 2.6 Frontend has almost no error handling  `Effort: M · P2`
**Issue:** Most components `fetch` with little/no error path; a 4xx/5xx/timeout renders as a generic
crash or nothing.

**How we'll solve it:** route all calls through the `lib/api.ts` wrapper that throws typed errors;
in each feature component show inline error states + a retry button; wrap pages with a Next.js
`error.tsx` boundary. Acceptance: killing the backend mid-use shows friendly errors, not a white screen.

**Impact:** Resilient, professional UX; users understand what went wrong and can recover.

## 2.7 No real health check  `Effort: S · P2`
**Issue:** `/api/home` is a static hello; it can't tell you if Groq/Pinecone are reachable.

**How we'll solve it:** add `GET /health` that does a cheap reachability probe of Groq and Pinecone
and returns `{status, groq, pinecone, version}` with 200/503. Use it for uptime monitoring and 2.5's
warm-up ping.

**Impact:** Real signal for monitoring/deploys; one call tells you what's actually up.

---

# PHASE 3 — DATA, GROUNDING & INTELLIGENCE  *(makes the product real, not a demo)*

## 3.1 Competitor/SWOT data is ungrounded LLM guesswork  `Effort: M · P2`
**Issue:** `companies.py`/`analysis.py` rely solely on LLM training knowledge — stale past cutoff and
prone to hallucination, with no citations. This is the core value prop and it's currently unreliable.

**How we'll solve it:**
1. Add a search provider (Tavily is simplest for LLM use; SerpAPI/Bing are alternatives). Store
   `TAVILY_API_KEY` in `.env`.
2. New `ml/services/search_service.py`: query "{company} competitors {location}" and recent news;
   collect top results (title, snippet, url).
3. Feed those snippets into the Groq prompt as grounding context and instruct the model to base the
   JSON on them and **include source URLs** per competitor/claim.
4. Surface citations in `Analysis.tsx`/`SWOTAnalysis` so users see where facts came from.

**Impact:** Current, defensible, citable analysis — turns the headline feature from "plausible-sounding" into "trustworthy."

## 3.2 Chatbots have no memory  `Effort: M · P2`
**Issue:** Only the current message is sent; the bot can't follow up — poor conversational UX.

**How we'll solve it:** change the chat request to accept `messages: [{role, content}]` (or a
`session_id`); keep the last N turns and pass them into the LangChain prompt via a
`history`-aware chain (or a `MessagesPlaceholder`). Store history client-side (state/localStorage)
short-term; move to DB (3.5) for persistence.

**Impact:** Real multi-turn conversations; the chatbots become genuinely useful.

## 3.3 No response streaming  `Effort: M · P3`
**Issue:** Every LLM reply waits for full generation before returning — feels slow.

**How we'll solve it:** stream from Groq and expose an SSE endpoint (FastAPI `StreamingResponse`);
on the frontend consume the stream and append tokens to the message bubble as they arrive.

**Impact:** Dramatically better perceived speed; modern chat UX.

## 3.4 RAG isn't reproducible  `Effort: M · P2`
**Issue:** Pinecone indexes must pre-exist; there's no committed way to rebuild them (see 0.7 Path B).

**How we'll solve it:** promote the 0.7 ingestion script to a documented, parameterized CLI
(`python -m chat.ingest --index chatbot1 --data ./data/medical --recreate`), commit the **source
docs** (or a fetch script) under `ml/chat/data/`, and document the steps in the README so anyone can
rebuild the knowledge base from scratch.

**Impact:** RAG is recoverable and onboardable; deleting an index is no longer catastrophic.

## 3.5 Nothing is persisted  `Effort: M · P2`
**Issue:** No DB — no users, saved analyses, chat history, or audit trail. Blocks history, metering, and admin.

**How we'll solve it:** add Postgres (e.g. Supabase/Neon free tier) with SQLAlchemy + Alembic
migrations; tables for `users` (keyed by Firebase uid), `analyses`, `chat_messages`. Save each
company/SWOT result and chat turn; add `GET /history` (authed). Wire a "Saved analyses" view in the
dashboard (2.4).

**Impact:** Users keep their work; unlocks history, metering (5.6), and admin — the jump from demo to product.

## 3.6 No caching of repeated LLM queries  `Effort: M · P3`
**Issue:** Identical company lookups re-hit Groq every time — wasted cost and latency.

**How we'll solve it:** cache keyed by normalized (company, location). Start with an in-process TTL
cache (`cachetools`); move to Redis when multi-instance. Optionally persist popular results in the DB (3.5).

**Impact:** Lower cost and instant repeat responses for common queries.

---

# PHASE 4 — PRODUCTION-GRADE ENGINEERING

## 4.1 No tests  `Effort: M · P2`
**Issue:** Zero automated tests → every change is a regression risk and the "production-ready" claim is hollow.

**How we'll solve it:** backend `pytest` with `httpx`/`TestClient` covering each endpoint (mock Groq/
Pinecone so tests are offline and free) + unit tests for the JSON parsing/validation (1.5). Frontend
`Vitest` + Testing Library for the feature components' loading/error/success states.

**Impact:** Confident refactors; regressions caught before merge; credibility for reviewers/interviewers.

## 4.2 No CI  `Effort: S · P2`
**Issue:** Nothing enforces lint/type/test on changes.

**How we'll solve it:** GitHub Actions workflow running, on PR: backend `ruff` + `pytest`; frontend
`eslint` + `tsc --noEmit` + `vitest`. Block merge on failure.

**Impact:** Automated quality gate; broken code can't reach main.

## 4.3 No containerization  `Effort: M · P3`
**Issue:** No one-command local stack; "works on my machine" deploy drift.

**How we'll solve it:** `ml/Dockerfile` (slim Python, pinned deps, pre-download the embedding model
into the image to avoid first-request lag) + root `docker-compose.yml` running backend + frontend
(+ Postgres from 3.5) together.

**Impact:** Reproducible environments; trivial local bring-up; consistent deploys.

## 4.4 No observability  `Effort: M · P3`
**Issue:** No structured logs, request tracing, or error monitoring — production failures are invisible.

**How we'll solve it:** structured JSON logging with a per-request id (middleware), response-time
logging, and Sentry on both backend and frontend for error capture.

**Impact:** You find out about failures before users do; debugging production becomes possible.

---

# PHASE 5 — PRODUCT POLISH & DIFFERENTIATORS

## 5.1 Finish or cut partially-built features  `Effort: S–M · P3`
**Issue:** Several half-features confuse users: GitHub OAuth provider exists with no button; 3/4
Sectors agents are "Coming Soon"; `/test` is a placeholder; chatbot quick-action buttons may not
actually send a message.
**How we'll solve it:** either complete each (add the GitHub sign-in button wired to `githubProvider`;
implement the 3 agents as simple Groq prompts; wire quick-actions to submit a pre-filled message) **or**
remove them from the UI until ready. Delete `/test`.
**Impact:** No dead-ends or broken buttons; the product feels finished.

## 5.2 Mobile chatbot + accessibility  `Effort: M · P3`
**Issue:** `ChatbotSmall` is a fixed 600px (breaks on phones); no ARIA/keyboard support anywhere.
**How we'll solve it:** make the widget responsive (`w-[90vw] max-w-[600px]`, full-screen sheet on
small breakpoints); add ARIA labels, focus management, and keyboard nav to interactive components.
**Impact:** Usable on phones; accessible to keyboard/screen-reader users.

## 5.3 SWOT/competitor AI disclaimer  `Effort: S · P3`
**Issue:** Ungrounded results are shown as fact with no caveat (until 3.1 lands, and even after).
**How we'll solve it:** add a small "AI-generated — verify before acting" note on analysis/SWOT views.
**Impact:** Sets honest expectations; reduces liability and builds trust.

## 5.4 Export reports  `Effort: M · P3`
**Issue:** No way to take competitor/SWOT results out of the app.
**How we'll solve it:** add "Download PDF/CSV" on the analysis view (client-side `jsPDF`/`react-pdf`,
or a backend render endpoint).
**Impact:** A shareable deliverable — a feature SME users actually want.

## 5.5 Repo hygiene cleanups  `Effort: S · P3`
**Issue:** Small professionalism gaps: `SWOTAnaylis.tsx` typo, unused `react-router-dom`, scratch
notebooks (`ml/1.ipynb`, `ml/companies.ipynb`) in the app dir, README run command.
**How we'll solve it:** rename `SWOTAnaylis.tsx` → `SWOTAnalysis.tsx` (update imports);
`npm rm react-router-dom`; move notebooks to `ml/notebooks/` (or delete); fix `README.md:55`
(`main:app` → `server:app`) if not already done in 0.3.
**Impact:** Cleaner, smaller, more credible repo.

## 5.6 Differentiators (big swings)  `Effort: L · P3`
**Issue:** To be a real "AI-as-a-service" product (and stand out), it needs monetization and unique value.
**How we'll solve it (each is its own project, needs 3.5 DB + 2.2 auth first):**
- **Usage metering + billing** (Stripe) — per-user quotas and plans.
- **Financial-data enrichment** — pull real revenue/headcount (Crunchbase/LinkedIn) to ground SWOT.
- **Competitor tracking** — let users "watch" a company and get scheduled AI update digests.
- **Multi-language output** — Hindi/regional languages for Indian SME users.
**Impact:** Turns a feature demo into a defensible, monetizable product.

---

## Dependency notes (ordering constraints)
- **Phase 0 before everything** — you can't validate fixes against a project that won't run.
- **Auth (2.2)** before **billing/metering (5.6)** and before exposing the backend publicly.
- **Database (3.5)** before **saved history, metering, admin**, and persistent **chat memory (3.2)**.
- **CI (4.2)** before large refactors so regressions are caught.
- **Config centralization (0.5) + Docker (4.3)** unblock clean multi-env deploys.

## Suggested first sprint
Finish **all of Phase 0** (mostly S-effort) → you have a running app. Then **1.1 (rotate/scrub keys)**
and **1.2 CORS** before sharing it anywhere. That gets you a safe, working baseline to build on.
