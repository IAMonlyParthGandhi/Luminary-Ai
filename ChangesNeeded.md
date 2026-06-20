# ChangesNeeded.md — Luminary AI

> Detailed, prioritized list of changes to make in the **current** version. Verified against
> source on **2026-06-20**. For full repo context see [CLAUDE.md](CLAUDE.md).
>
> **Context:** The owner plans to rebuild the *idea, ML, and backend* largely **from scratch**.
> So this file is split into:
> - **§A Security** — do regardless of rewrite (leaked keys are leaked NOW).
> - **§B Bugs & fixes** — only worth touching if you keep the current backend; otherwise just
>   *avoid repeating* them in the rewrite.
> - **§C Missing features** — the real backlog to design into the new version.
> - **§D Phased plan** and **§E carry-forward vs drop** — to steer the rewrite.
>
> Severity: 🔴 CRITICAL · 🟠 HIGH · 🟡 MEDIUM · ⚪ LOW.

---

## ✅ Already done in this pass (safe, non-structural)

- **Added a root `.gitignore`** covering `.env`/`.env.*`, virtualenvs, `__pycache__`,
  `node_modules`, Next.js `.next/`, build output, and `model.pkl`. The repo previously had **no
  `.gitignore` at all**, which is how secrets and a virtualenv got committed in the first place.
  This prevents it recurring in the rewrite. *(No project code/structure was changed.)*

> Note: `ml/.env`, virtualenvs, and `__pycache__` are **no longer in the working tree or index**
> (already removed in an earlier commit). The remaining problem is **git history** — see §A.1.

---

## §A. Security — do this regardless of the rewrite

### A.1 🔴 Leaked API keys still in git history — `ml/.env`
`ml/.env` (with real `PINECONE_API_KEY`, `OPENAI_API_KEY`, `HUGGINGFACEHUB_API_TOKEN`,
`GROQ_API_KEY`, `REPLICATE_API_TOKEN`) was committed in earlier commits (`a5382e8 "ml uploaded"`,
`3eba29d "Done Some Importnt Changes"`). It's gone from the current tree but **still recoverable
from history** — assume every key is compromised.

**Do, in order (these are destructive / outward-facing — run them yourself):**
1. **Rotate every key now** in each provider's dashboard (Groq, Pinecone, HuggingFace, OpenAI,
   Replicate). This is the only step that actually stops abuse.
2. Add `ml/.env.example` with empty placeholders for onboarding.
3. **Scrub history** so the keys leave past commits, e.g.:
   ```bash
   pip install git-filter-repo
   git filter-repo --path ml/.env --invert-paths
   git push --force --all     # coordinate with anyone who has a clone
   ```
   (Or use BFG.) Note this rewrites every commit hash.

### A.2 🟠 Restrict CORS — `ml/server.py:16-22`
Currently `allow_origins=["*"]` **with** `allow_credentials=True` — an invalid combo browsers
reject, and wide open.
```python
import os
origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")
app.add_middleware(CORSMiddleware,
    allow_origins=origins, allow_credentials=True,
    allow_methods=["GET", "POST"], allow_headers=["*"])
```

### A.3 🟠 No auth / rate limiting on paid endpoints — all `ml/routes/*`, `server.py`
Every AI route is public; each call burns Groq/Pinecone quota → trivial to abuse.
- Verify the Firebase ID token on the backend (`firebase-admin`) as a FastAPI dependency, **or**
  a shared-secret header at minimum.
- Add rate limiting (e.g. `slowapi`) keyed by IP / API key.
- Add input length limits (a 100k-char chatbot message is billed and may error).

---

## §B. Bugs & fixes in the current backend/frontend

| # | Sev | Issue | Location | Fix |
|---|---|---|---|---|
| 1 | 🟠 | Hardcoded backend URL duplicated | `Analysis.tsx`, `Chatbot.tsx`, `ChatbotSmall.tsx`, `CompanyInput.tsx`, `StartForm.tsx` | Centralize via `NEXT_PUBLIC_API_URL` (below) |
| 2 | 🟠 | Unpinned Python deps + duplicate line | `ml/requirements.txt` | Pin with `==`; remove duplicate `langchain-pinecone`; drop unused (`langchain-openai`?, `pandas`, `pypdf` if unused) |
| 3 | 🟡 | Bare `except` leaks raw error w/ HTTP 200 | `ml/server.py:40-43` | Log server-side; return generic message + proper status (match `/companies-analysis` which raises 400) |
| 4 | 🟡 | Fragile LLM JSON parsing | `companies.py`, `analysis.py` | Use Groq JSON mode + validate with Pydantic; fail gracefully |
| 5 | 🟡 | RAG re-initialized every request | `ml/services/chat_service.py`, `marketing_chatbot_service.py` | Init embeddings + index once at startup (FastAPI `lifespan`), reuse the chain |
| 6 | 🟡 | README run command wrong | `README.md:55` | `uvicorn main:app` → `uvicorn server:app` |
| 7 | ⚪ | "medical-bot" / `chatbot1` naming inherited from a medical template | `routes/chat_routes.py`, indexes | Rename route + index to the real domain; confirm indexed corpus matches |
| 8 | ⚪ | Component filename typo | `SWOTAnaylis.tsx` | Rename to `SWOTAnalysis.tsx` |
| 9 | ⚪ | Dead dependency | `frontend/package.json` | Remove unused `react-router-dom` |
| 10 | ⚪ | Scratch notebooks in app dir | `ml/1.ipynb`, `ml/companies.ipynb` | Move to a `notebooks/` dir or remove from the deployed backend |

**Centralized API base URL (fix #1):**
```ts
// frontend/src/lib/api.ts
export const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";
```
Import everywhere; set `NEXT_PUBLIC_API_URL` in `.env.local` / Vercel.

---

## §C. Missing features (the real backlog for the new version)

**Blocking / core UX**
- ❌ **`/dashboard` page** — login redirects to `/dashboard`, which doesn't exist → **404**.
- ❌ **Route guards** — no auth gate; any page is reachable without login.
- ❌ **Live web search for competitor/SWOT data** — currently stale LLM knowledge. Add
  Tavily / SerpAPI / Bing to ground results (this was the original hackathon plan).
- ❌ **Conversation memory in chatbots** — send last N message pairs; bots are fully stateless.
- ❌ **Response streaming** — Groq supports SSE; stream tokens for perceived speed.
- ❌ **Render cold-start UX** — show a "server waking up…" banner + retry instead of a silent hang.
- ❌ **Frontend error handling** — most fetches have no error boundary; a 503 cold start looks like a crash.

**Data & reproducibility**
- ❌ **Database** (e.g. Postgres) — nothing persists: no users, saved analyses, or chat history.
- ❌ **Knowledge-base ingestion script** — Pinecone indexes must be pre-populated; no script ships
  to recreate them from PDFs/docs.
- ❌ **Response caching** — identical company lookups re-hit Groq every time.
- ❌ **Query history** (at least localStorage) — let users revisit past searches.

**Quality / production-readiness**
- ❌ **Tests** (pytest for `companies.py`/`analysis.py`/services; Vitest/Jest for FE).
- ❌ **CI** (GitHub Actions: lint + type-check + tests).
- ❌ **`/health`** endpoint that checks Groq + Pinecone reachability.
- ❌ **Structured logging / observability** (request IDs, Sentry, latency metrics).
- ❌ **`docker-compose.yml`** for a one-command local stack.
- ❌ **Input validation / sanitization** beyond default Pydantic.
- ❌ **Accessibility** (ARIA, keyboard nav, focus management).
- ❌ **Mobile chatbot** — `ChatbotSmall` is fixed 600px → breaks on phones.
- ❌ **SWOT disclaimer** — make clear results are AI-generated and may be inaccurate.
- ❌ **PDF/CSV export** of competitor/SWOT reports.

**Partially built (finish or cut)**
- ⚠️ **GitHub OAuth** — provider configured in `firebase.ts`, no sign-in button in `Signin.tsx`.
- ⚠️ **Sectors agents** — only Healthcare works; AI Consultant / Business Advisor / Analytics are "Coming Soon".
- ⚠️ **`/test` page** — placeholder; remove or repurpose.
- ⚠️ **Chatbot quick-action buttons** — may not actually send a pre-filled message; verify handlers.

---

## §D. Phased plan (if evolving rather than full rewrite)

Effort: S (<½ day) · M (1–3 days) · L (1+ week).

**Phase 1 — Security & correctness (blocking)**
- Rotate keys, scrub history, add `.env.example` (FE + BE) — §A.1 · S
- Lock down CORS — §A.2 · S
- Centralize frontend API URL via env — §B.1 · S
- Pin Python deps; dedupe `requirements.txt` — §B.2 · S
- Fix README run command — §B.6 · S

**Phase 2 — Reliability & UX**
- Enforce auth on AI endpoints (Firebase admin verify) — §A.3 · M
- Rate limiting + consistent error envelopes — §A.3/§B.3 · M
- RAG init once at startup — §B.5 · S
- Robust LLM JSON (Groq JSON mode + Pydantic) — §B.4 · M
- Add a database (Postgres) for users + saved analyses · M
- `/dashboard` + route guards · M
- Minimal test suite + GitHub Actions CI · M

**Phase 3 — Scale & polish**
- Live web search grounding (Tavily/SerpAPI) · M
- Conversation memory + streaming · M
- Caching for repeated LLM queries · M
- Dockerize + deploy pipeline · M
- Observability (logging, Sentry, metrics) · M
- Usage metering + billing (Stripe) for the "AI-as-a-service" model · L
- Admin dashboard / analytics · L

**Dependencies:** Auth precedes billing. DB precedes saved history/metering/admin. CI precedes big
refactors. Config centralization unblocks Docker/multi-env deploys.

---

## §E. For the from-scratch rewrite — carry forward vs drop

**Carry forward (works / good calls)**
- The 5-feature product framing (competitor + SWOT, branding/taglines, SEO, RAG chatbots).
- Groq for fast/cheap inference; FastAPI; Next.js 15 App Router; shadcn/ui.
- Clean `routes/` + `services/` separation in the backend.

**Design in from day one (the gaps above)**
- A `.gitignore` + `.env.example` before the first commit (done — keep it). Never commit secrets.
- Backend auth + rate limiting + input limits on any paid LLM route.
- A real datastore and a Pinecone-ingestion script so RAG is reproducible.
- Live web-search grounding for competitor/SWOT (don't ship ungrounded LLM "facts").
- Env-driven config (API base URL, allowed origins) — no hardcoded URLs.
- Streaming + conversation memory for chatbots.
- Tests + CI from the start.

**Drop / don't recreate**
- Committed `.env` / virtualenv / `__pycache__` (gitignore handles this now).
- Unused deps (`react-router-dom`, `langchain-openai`/`pandas`/`pypdf` if unused, `OPENAI_API_KEY`,
  `REPLICATE_API_TOKEN`).
- "medical-bot"/`chatbot1` template naming — name things for the real domain.
- Filename typos (`SWOTAnaylis.tsx`) and scratch notebooks in the deployed dir.
