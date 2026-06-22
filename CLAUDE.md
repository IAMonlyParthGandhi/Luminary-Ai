# CLAUDE.md — Luminary AI Master Context Pack

> **What this file is:** The single document to paste into any AI assistant (Claude, GPT,
> etc.) to give it full context on this repo in the fewest tokens — it replaces pasting
> source code. Verified against the actual source on **2026-06-21** (post-restructure).
>
> **Companion file:** [ROADMAP.md](ROADMAP.md) — the run-first, phased plan with detailed,
> executable steps for every fix/change (issue → how to solve → impact).
>
> **Heads-up:** The repo was just **restructured** (backend `ml/` → `backend/app/` package;
> frontend components regrouped into feature folders) with all logic preserved. The owner may
> still rework the *idea/ML* later; treat the specifics below as the current, post-refactor state.

---

## 1. Identity & Elevator Pitch

| Field | Value |
|---|---|
| **Project** | Luminary AI |
| **Pitch** | AI-as-a-service for small/mid-sized businesses (SMEs): competitor discovery + **SWOT**, AI **branding/tagline** generation, domain **RAG chatbots**, and **SEO** help. |
| **Tagline** | *"Harness AI agents for powerful solutions."* |
| **Author** | Parth Gandhi, B.Tech CSE, SVNIT Surat |
| **Team** | "404 Not Found" |
| **Origin** | DotSlash Hackathon (ACM + SVNIT + ASHINE Incubation Cell) |
| **Shape** | Monorepo: **Next.js** frontend (`frontend/`) + **FastAPI** backend (`backend/`) wrapping **Groq** LLMs, a **Pinecone** vector store, and **LangChain** RAG. |
| **Deploy** | Frontend → Vercel · Backend → Render free tier (cold-start issue) |
| **Backend live URL** | `https://dotslash-backend.onrender.com` (now configurable via `NEXT_PUBLIC_API_URL` — see ROADMAP 0.5) |

> The team also calls the backend "DotSlash"; the Render URL reflects that.

---

## 2. Tech Stack (from manifests)

**Frontend (`frontend/`)**
| Layer | Tech | Version |
|---|---|---|
| Framework | Next.js (App Router) + React | `next 15.1.6`, `react 19.0.0` |
| Language | TypeScript | `^5` |
| Styling | Tailwind CSS + shadcn/ui + Radix | `tailwindcss 3.4.1` |
| Animation | framer-motion | `^12.0.6` |
| Icons | lucide-react | `0.474` |
| Auth (client) | Firebase Auth (Email/pw, Google, GitHub providers) | `firebase ^11.2.0` |
| Email | Nodemailer + Handlebars (Gmail SMTP) | `nodemailer ^6.10.0` |
| Markdown | react-markdown | `^9.0.3` |

**Backend (`backend/`)** — ⚠️ **all Python deps are still unpinned** (no `==`); the refactor
removed the duplicate `langchain-pinecone` line and the unused deps.
| Layer | Tech |
|---|---|
| Framework | FastAPI (`fastapi[all]`) |
| LLM — primary | Groq `llama-3.3-70b-versatile` (company info, SWOT, taglines, SEO) |
| LLM — chatbots | Groq `deepseek-r1-distill-llama-70b` (`<think>` tags stripped) |
| Embeddings | `sentence-transformers/all-MiniLM-L6-v2` (384-D, local HF) |
| Vector DB | Pinecone — indexes `chatbot1`, `chatbot2` (one merged RAG service serves both) |
| RAG | LangChain (community/groq/pinecone) |
| Config | `python-dotenv` (`backend/.env`); `backend/.env.example` committed |
| Removed in refactor | duplicate `langchain-pinecone`, `langchain-openai`, `langchain-experimental`, `pandas`, `pypdf`, `react-router-dom`, scratch notebooks, `egg-info/`, `model.pkl` |

---

## 3. Repo Map (meaningful files; ignore `node_modules`, `__pycache__`, any `.venv`)

```
Luminary-Ai/
├── README.md                 # Setup guide (now correct: `cd backend`, `uvicorn main:app`)
├── CLAUDE.md                 # ← this file (consolidated context)
├── ROADMAP.md                # run-first phased plan: issue → how to solve → impact
├── PromptForContextGathering.md  # (leftover meta-prompt to regenerate docs)
│
├── frontend/                 # Next.js 15 app
│   └── src/
│       ├── app/              # App Router pages (route filenames fixed by Next.js)
│       │   ├── page.tsx          # Home (Navbar, Hero, Work, Sponsors, Footer)
│       │   ├── build/page.tsx    # SEO + tagline generator (StartForm)
│       │   ├── chat/page.tsx     # Full-page chatbot (Chatbot)
│       │   ├── explore/page.tsx  # Company research (CompanyInput + ChatbotSmall)
│       │   ├── sectors/page.tsx  # Agent showcase (ChatbotCard)
│       │   ├── signin|signup/    # Firebase auth pages
│       │   ├── contact|team|sponsors/
│       │   ├── layout.tsx        # Root layout, Geist font
│       │   └── globals.css
│       ├── components/       # grouped by feature
│       │   ├── layout/   # Navbar, Footer
│       │   ├── home/     # Hero, Work, Sponsors, DotMatrixText
│       │   ├── company/  # CompanyInput (→ GET /company), Analysis (→ POST /companies-analysis, SWOT inline), MultiStepLoader
│       │   ├── build/    # StartForm (→ GET /seo + POST /tagline-generator)
│       │   ├── chat/     # Chatbot (→ /medical-bot), ChatbotSmall (→ /marketing-bot), ChatbotCard
│       │   ├── auth/     # Signin, Signup
│       │   ├── contact/  # ContactUs, Team
│       │   └── ui/       # shadcn primitives (button, card, input, label, alert, scroll-area)
│       ├── hooks/sendMail.tsx      # server action → lib/mail.ts (to mjgandhi2305@gmail.com)
│       └── lib/
│           ├── api.ts              # API_BASE_URL (NEXT_PUBLIC_API_URL ?? localhost:8000) — single source of truth
│           ├── firebase.ts         # auth + Google/GitHub providers (NEXT_PUBLIC_* vars)
│           ├── mail.ts             # Nodemailer Gmail SMTP
│           ├── templates/welcome.ts
│           └── utils.ts            # cn() Tailwind merge
│
└── backend/                  # FastAPI backend (entry: backend/main.py → `uvicorn main:app`)
    ├── main.py               # App, CORS(*), GET /api/home; mounts the 4 routers
    ├── requirements.txt      # unpinned deps (duplicate + unused removed)
    ├── .env.example          # GROQ / PINECONE / HUGGINGFACEHUB placeholders
    └── app/
        ├── config.py         # loads GROQ_API_KEY, PINECONE_API_KEY, HUGGINGFACEHUB_API_TOKEN
        ├── core/
        │   ├── groq.py       # shared Groq client (getClient) + parseJson() helper
        │   ├── embeddings.py # downloadHuggingFaceEmbeddings()
        │   └── prompts.py    # CHATBOT_SYSTEM_PROMPT (one prompt, both bots)
        ├── routers/
        │   ├── company.py    # GET /company + POST /companies-analysis
        │   ├── chat.py       # POST /medical-bot + POST /marketing-bot
        │   ├── taglines.py   # POST /tagline-generator
        │   └── seo.py        # GET  /seo
        └── services/
            ├── company.py    # getCompanyInfo() — company + 5 competitors (Groq)
            ├── analysis.py   # companiesAnalysis() — SWOT for first 3 companies (Groq)
            ├── chat.py       # MERGED RAG: getChatResponse(msg, domain); Pinecone + Groq deepseek; strips <think>
            ├── taglines.py   # generateTaglines() — 5 names + taglines (Groq)
            └── seo.py        # getSeo() — 10 SEO keywords (Groq)
```

> ⚠️ A root `.gitignore` covers `.env`, virtualenvs, `__pycache__`, `node_modules`, build output,
> etc. `ml/.env`, virtualenvs, and `__pycache__` were committed in the past; they are no longer in
> the working tree but **the leaked keys remain in git history** (old path `ml/.env`). See ROADMAP 1.1.

---

## 4. Architecture & Data Flow

```
Browser (Next.js, :3000)
   │  fetch() → API_BASE_URL (lib/api.ts): NEXT_PUBLIC_API_URL or http://localhost:8000
   ▼
FastAPI (backend/main.py, :8000)
   ├─ GET  /api/home          → inline {message, team}
   ├─ GET  /company           → services.company.getCompanyInfo()       → Groq llama-3.3-70b
   ├─ POST /companies-analysis→ services.analysis.companiesAnalysis()   → Groq llama-3.3-70b (SWOT, first 3)
   ├─ POST /medical-bot       → services.chat.getChatResponse(_, "medical")   → RAG: Pinecone(chatbot1)
   │                                                              + HF embeddings + Groq deepseek
   ├─ POST /marketing-bot     → services.chat.getChatResponse(_, "marketing") → RAG: Pinecone(chatbot2)
   ├─ POST /tagline-generator → services.taglines.generateTaglines()    → Groq
   └─ GET  /seo               → services.seo.getSeo()                   → Groq

Both chatbots share ONE service (services/chat.py), differing only by Pinecone index.
Company/analysis/taglines/seo share core/groq.py (client + JSON parsing).
Firebase Auth (client-side ONLY): Email/pw + Google (+ GitHub provider configured, no button).
Email: lib/mail.ts (Nodemailer + Handlebars) → contact form → mjgandhi2305@gmail.com.
```

**Key characteristics**
- **No database.** All "data" is generated per-request by LLM calls. Pinecone holds only the
  chatbot vector indexes. Nothing (users, sessions, analyses, chat history) is persisted.
- **Auth and backend are disconnected.** Firebase login happens in the browser; FastAPI
  endpoints verify **no** token — every AI endpoint is publicly callable and spends paid quota.
- **RAG chatbots are stateless** — only the current message is sent; no conversation memory.
- **Competitor/SWOT data is pure LLM knowledge** — no live web search (the hackathon's Bing
  Search pipeline is NOT in this codebase), so results are stale past the model cutoff and
  ungrounded. No accuracy disclaimer shown.

---

## 5. Endpoint Inventory

| Method | Path | Request | Calls | Notes |
|---|---|---|---|---|
| GET | `/api/home` | — | inline (`main.py`) | Health/hello + team names `['Vatsal','Miten','Laskhit']` |
| GET | `/company` | `?company`, `?location` | `services.company.getCompanyInfo` | Company + 5 competitors JSON. **Bare `except` returns `{error: str(e)}` with HTTP 200** (`routers/company.py`) |
| POST | `/companies-analysis` | JSON body (company info) | `services.analysis.companiesAnalysis` | SWOT for **first 3** companies; raises `HTTPException(400)` on error |
| POST | `/medical-bot` | `{ "msg": str }` | `services.chat.getChatResponse(_, "medical")` | RAG over Pinecone `chatbot1` |
| POST | `/marketing-bot` | `{ "msg": str }` | `services.chat.getChatResponse(_, "marketing")` | RAG over Pinecone `chatbot2` |
| POST | `/tagline-generator` | `{ company_description, company_sector }` | `services.taglines.generateTaglines` | 5 names + taglines |
| GET | `/seo` | `?company_description`, `?location` | `services.seo.getSeo` | 10 SEO keywords |

No API versioning, no pagination, **no auth, no rate limiting, no input length limits**.
Swagger UI auto-available at `/docs`.

---

## 6. Backend Component Notes (current behavior)

- **`main.py`** — CORS `allow_origins=["*"]` + `allow_credentials=True` (preserved from before; invalid
  combo on paper but fine for the current no-credentials frontend). No auth/rate-limit/logging middleware.
- **`core/groq.py`** — `getClient()` (shared Groq client) + `parseJson()` (strip ```` ```json ```` fences →
  `json.loads`). Used by company/analysis/taglines/seo — the fragile JSON parsing now lives in **one place**.
- **`services/company.py` `getCompanyInfo(name, location, api_key)`** — Groq `llama-3.3-70b`, temp 0.3,
  max_tokens 1000. Structured-JSON prompt (official_name, industry_type, headquarters,
  key_products_services[], website, competitors[5]). LLM knowledge only; no web search; no retry.
- **`services/analysis.py` `companiesAnalysis(company_info, api_key)`** — top 3 companies → Groq → SWOT.
- **`services/chat.py`** (merged RAG) — `getChatResponse(msg, domain)` with
  `INDEXES = {"medical": "chatbot1", "marketing": "chatbot2"}`. HF `all-MiniLM-L6-v2` (384-D) → Pinecone →
  `k=3` → LangChain retrieval chain → Groq `deepseek-r1-distill-llama-70b` → strip `<think>`. Prompt:
  `core/prompts.CHATBOT_SYSTEM_PROMPT` (the two formerly-identical prompts are now one). ⚠️ Still
  **re-initializes embeddings + index on EVERY request** (ROADMAP 2.1). Indexes must pre-exist.
- **`services/seo.py` `getSeo(desc, location)`** — fetches a company profile then 10 SEO keywords. LLM only.
- **`services/taglines.py` `generateTaglines(desc, sector, api_key)`** — Groq `llama-3.3-70b` → 5 `{name, TagLine}`.
- **`core/embeddings.py`** — `downloadHuggingFaceEmbeddings()` (still uses the deprecated
  `from langchain.embeddings import HuggingFaceEmbeddings` import — ROADMAP 0.1).

---

## 7. Environment Variables

**Backend (`backend/.env`, loaded by `app/config.py` via `python-dotenv`; template in `backend/.env.example`)**
| Var | Used in | Purpose |
|---|---|---|
| `GROQ_API_KEY` | `config.py`, services | Groq LLM calls (required) |
| `PINECONE_API_KEY` | `services/chat.py` | Pinecone vector store |
| `HUGGINGFACEHUB_API_TOKEN` | `core/embeddings.py` | HF embeddings download |

> `OPENAI_API_KEY` / `REPLICATE_API_TOKEN` appeared in the *old* committed `.env` but were never used by
> the code; their LangChain deps were removed in the refactor.

**Frontend (`.env.local`, not in repo — set on Vercel)**
```
NEXT_PUBLIC_FIREBASE_API_KEY=
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=
NEXT_PUBLIC_FIREBASE_PROJECT_ID=
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=
NEXT_PUBLIC_FIREBASE_APP_ID=
SMTP_EMAIL=        # Gmail address for contact form
SMTP_PASSWORD=     # Gmail app password
NEXT_PUBLIC_API_URL=http://localhost:8000   # consumed by lib/api.ts
```

> 🔴 **Security:** real keys (Pinecone, OpenAI, HuggingFace, Groq, Replicate) were committed in
> `ml/.env` in earlier commits and **still live in git history**. Rotate all + scrub history.
> See ROADMAP 1.1.

---

## 8. How to Run

**Frontend**
```bash
cd frontend
npm install
npm run dev        # http://localhost:3000  (uses --turbopack)
```

**Backend**
```bash
cd backend
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env   # then fill GROQ_API_KEY (+ PINECONE_API_KEY, HUGGINGFACEHUB_API_TOKEN)
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

> ⚠️ The frontend reads `NEXT_PUBLIC_API_URL` via `lib/api.ts` (defaults to `http://localhost:8000`);
> set it to point at a remote backend. No test suite, no CI.
> ⚠️ RAG chatbots need pre-populated Pinecone indexes (`chatbot1`, `chatbot2`); no ingestion
> script ships in the repo (see ROADMAP 0.7).

---

## 9. Status at a Glance

| Feature | Status | Note |
|---|---|---|
| Company + competitor lookup (`/company`) | ✅ Working | Groq-backed, LLM-knowledge only |
| SWOT (`/companies-analysis`) | ✅ Working | First 3 companies; ungrounded |
| Tagline generator (`/tagline-generator`) | ✅ Working | 5 names + taglines |
| SEO (`/seo`) | ✅ Working | LLM-only keywords |
| Medical RAG chatbot (`/medical-bot`) | ⚠️ Partial | Needs pre-built Pinecone `chatbot1` |
| Marketing RAG chatbot (`/marketing-bot`) | ⚠️ Partial | Needs pre-built Pinecone `chatbot2` |
| Firebase auth (frontend) | ⚠️ Partial | Client sign-in only; not enforced on backend; GitHub provider has no button |
| Contact email | ✅ Working | Nodemailer Gmail SMTP (needs SMTP env) |
| Dashboard / route guards | ❌ Missing | Login redirects to `/dashboard` → **404** |
| Live web search for competitors | ❌ Missing | Stale LLM knowledge only |
| Conversation memory / streaming | ❌ Missing | Bots stateless; responses non-streamed |
| Persistence / DB | ❌ None | — |
| Tests / CI / Docker | ❌ None | — |
| Observability / logging | ❌ None | — |

---

## 10. Performance & Resource Profile

| Stage | Latency |
|---|---|
| Render cold start (worst) | 2–5 min (no "waking up" UI → looks like a hang) |
| Groq company info / SWOT / taglines | ~1–4 s |
| HF embed + Pinecone search | ~300–600 ms |
| Chatbot response total | ~2–4 s |
| Company research flow total | ~4–8 s |

Backend RAM ~500 MB–1 GB (sentence-transformers loaded in memory). Frontend on Vercel
serverless. No GPU (all inference via Groq cloud).

---

## 11. Architecture Decisions (rationale)

| Decision | Why |
|---|---|
| Groq over OpenAI | Free, ultra-fast LPU inference; fine for demo |
| Pinecone | Managed, free tier, fast similarity search |
| Local sentence-transformers embeddings | Free, no per-call cost; 384-D enough for RAG |
| FastAPI over Flask | Pydantic validation, async, auto Swagger |
| Next.js 15 App Router | Server/client split, Vercel-native SSR |
| Firebase Auth | Free OAuth without a custom auth server |
| Render / Vercel free tiers | Zero-cost demo hosting |
| LLM-only competitor data | Bing Search pipeline existed at hackathon but was never committed |
| One merged RAG service | Medical/marketing bots were identical bar the index → parameterized by domain |

---

## 12. Known Issues → see [ROADMAP.md](ROADMAP.md)

Top risks (full detail + executable fixes in ROADMAP.md):
1. 🔴 **Leaked API keys in git history** (`ml/.env`) — rotate all + scrub history.
2. 🟠 **CORS** `*` + credentials (`main.py`) — preserved; lock down for prod.
3. 🟠 **No auth/rate-limit** on paid LLM endpoints — cost & abuse risk.
4. 🟠 **Unpinned Python deps** — duplicate + unused removed, but still need `==` pinning.
5. 🟡 **Bare `except`** (`routers/company.py`); **fragile LLM JSON parsing** (now centralized in `core/groq.py`); **RAG re-init per request** (`services/chat.py`).
6. ❌ Missing: `/dashboard` + route guards, live web search, conversation memory, tests/CI/Docker, observability.

> ✅ Resolved by the restructure: hardcoded backend URL (now `lib/api.ts`), duplicate `langchain-pinecone`,
> unused deps, `react-router-dom`, README run command, `SWOTAnaylis` typo (file was dead → deleted),
> scratch notebooks / `egg-info` / `model.pkl`.
```
