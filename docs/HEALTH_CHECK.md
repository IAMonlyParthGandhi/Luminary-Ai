# HEALTH_CHECK.md — Luminary AI

> Fast read on what works, what's broken, and what to do next. Generated from code on
> **2026-06-20**. For deep detail see `ISSUES_AND_FIXES.md` and `ROADMAP.md`.

## ✅ Working Well
- **Clean FastAPI structure** — routers in `ml/routes/`, logic in `ml/services/`; easy to extend.
- **Multiple AI features implemented end-to-end**: company lookup, SWOT analysis, tagline
  generation, two chatbots, SEO — all wired to Groq.
- **Modern frontend stack** — Next.js 15 App Router, React 19, Tailwind + shadcn/ui,
  framer-motion; component-per-feature layout is readable.
- **Firebase auth** scaffolded with Google + GitHub providers using `NEXT_PUBLIC_*` env vars.
- **RAG pipeline** with sane defaults (top-3 retrieval, `<think>` stripping).

## 🐞 Problems / Bugs
- 🔴 **Secrets in git**: `ml/.env` with live keys is committed.
- 🔴 **`ml/.venv/` committed**: massive vendored tree tracked despite `.gitignore`.
- 🟠 **Broken docs**: README's `uvicorn main:app` doesn't match entry `server.py`.
- 🟠 **Insecure CORS**: `allow_origins=["*"]` with `allow_credentials=True`.
- 🟠 **Hardcoded backend URL** (`dotslash-backend.onrender.com`) duplicated across
  components — local dev and redeploys break silently.
- 🟡 **Bare `except`** in `/company` returns raw exception text to the client.
- 🟡 **Fragile LLM JSON parsing** — relies on regex-stripping ```` ```json ````; any
  malformed model output throws.

## 🚧 Incomplete / Stubbed
- **Auth not enforced** on the backend — Firebase login is cosmetic for API protection.
- **`/medical-bot` naming** suggests a reused medical RAG template; confirm the index
  `chatbot1` content matches Luminary's domain.
- **`services/model.pkl`** — a pickled model with unclear provenance/usage.
- **No persistence** — nothing is saved between requests.
- **Email/contact** path needs SMTP env verification.

## 🚨 Urgent (do first)
1. Rotate all leaked keys and untrack `ml/.env`.
2. Untrack `ml/.venv/` and `__pycache__`.
3. Fix README run command.

## 💡 Nice-to-Have
- Pin dependency versions; add `.env.example` files.
- Centralize the API base URL via `NEXT_PUBLIC_API_BASE_URL`.
- Add request/response validation models and consistent error envelopes.
- Add a minimal test suite + GitHub Actions CI.
- Dockerize backend for reproducible deploys.

## 🎯 Top 5 Things To Do Next (ranked)
| # | Action | Effort | Impact |
|---|---|---|---|
| 1 | Rotate keys, untrack `.env`, scrub history | S | 🔴 Critical |
| 2 | Untrack `.venv`/`__pycache__`, fix `.gitignore` | S | High |
| 3 | Centralize API base URL + add `.env.example` | S | High |
| 4 | Lock down CORS + add rate limiting/auth on AI endpoints | M | High |
| 5 | Pin deps + add CI + smoke tests | M | Medium |
