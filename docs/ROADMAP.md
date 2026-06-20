# ROADMAP.md — Luminary AI

> What's done, what's missing, and a phased plan. Generated **2026-06-20**.
> Effort: S (<½ day) · M (1–3 days) · L (1+ week).

## ✅ Completed (verified in code)
- Company + competitor discovery (`/company`).
- SWOT analysis for top 3 companies (`/companies-analysis`).
- Tagline/branding generation (`/tagline-generator`).
- RAG chatbot (`/medical-bot`) + marketing chatbot (`/marketing-bot`).
- SEO helper (`/seo`).
- Next.js frontend with pages + components wired to the above.
- Firebase client auth (Google + GitHub).

## 🧩 Gaps / Missing Standard Features
- **No backend auth/authorization** — Firebase login isn't enforced on the API.
- **No database** — nothing persists (no user history, saved analyses, or audit trail).
- **No usage metering / billing** — needed for a real "AI-as-a-service" product.
- **No tests, no CI, no Docker** — releases are manual and unverified.
- **No observability** — no logging/metrics/error monitoring.
- **No input validation/rate limiting** — abuse and cost exposure.
- **Config not externalized** — hardcoded URLs; unpinned deps.

## 🗺️ Phased Plan

### Phase 1 — Security & Correctness (blocking) 
| Item | Effort |
|---|---|
| Rotate keys, untrack `ml/.env`, scrub history | S |
| Untrack `.venv`/`__pycache__`; fix `.gitignore` | S |
| Fix README (`uvicorn server:app`) | S |
| Lock down CORS to known origins | S |
| Centralize frontend API base URL via env | S |
| Pin Python deps; add `.env.example` (FE + BE) | S |

### Phase 2 — Reliability & UX 
| Item | Effort |
|---|---|
| Enforce auth on AI endpoints (Firebase admin token verify) | M |
| Rate limiting (`slowapi`) + structured error envelopes | M |
| Initialize RAG once at startup (FastAPI lifespan) | S |
| Robust LLM JSON (Groq JSON mode + Pydantic validation) | M |
| Add a database (Postgres) for users + saved analyses | M |
| Minimal test suite + GitHub Actions CI | M |

### Phase 3 — Scale & Polish 
| Item | Effort |
|---|---|
| Usage metering + billing (Stripe) | L |
| Dockerize backend; deploy pipeline | M |
| Observability (logging, Sentry, metrics) | M |
| Caching layer for repeated LLM queries | M |
| Admin dashboard / analytics | L |

## 🔗 Dependencies Between Items
- Auth (P2) should land before billing/metering (P3).
- Database (P2) is a prerequisite for saved history, metering, and admin dashboard.
- CI (P2) should precede larger refactors so regressions are caught.
- Config centralization (P1) unblocks Docker/multi-env deploys (P3).

## 🚀 Suggested First Sprint
Knock out **all of Phase 1** (mostly S-effort, high impact), then start **auth +
rate limiting** from Phase 2. That removes the critical security exposure and makes the
service safe to run publicly before investing in DB/billing.
