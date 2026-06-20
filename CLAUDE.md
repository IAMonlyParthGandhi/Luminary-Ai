# CLAUDE.md — Luminary AI Master Context Pack

> **What this file is:** The single document to paste into any AI assistant (Claude, GPT,
> etc.) to give it full context on this repo in the fewest tokens — it replaces pasting
> source code. Everything here was verified against the actual source on **2026-06-20**.
>
> **Companion file:** [ChangesNeeded.md](ChangesNeeded.md) — the prioritized, detailed list
> of fixes/changes to make in the current version (security, bugs, missing features, roadmap).
>
> **Heads-up:** The owner intends to rebuild the *idea, ML, and backend* largely **from
> scratch**. Treat the backend specifics below as the *current* state to learn from and
> carry forward — not a contract to preserve.

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
| **Shape** | Monorepo: **Next.js** frontend (`frontend/`) + **FastAPI** backend (`ml/`) wrapping **Groq** LLMs, a **Pinecone** vector store, and **LangChain** RAG. |
| **Deploy** | Frontend → Vercel · Backend → Render free tier (cold-start issue) |
| **Backend live URL** | `https://dotslash-backend.onrender.com` (hardcoded in frontend — see ChangesNeeded #5) |

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
| Dead weight | `react-router-dom` (installed, unused — Next handles routing) | — |

**Backend (`ml/`)** — ⚠️ **all Python deps are unpinned** (no `==`), and `requirements.txt`
lists `langchain-pinecone` twice.
| Layer | Tech |
|---|---|
| Framework | FastAPI (`fastapi[all]`) |
| LLM — primary | Groq `llama-3.3-70b-versatile` (company info, SWOT, taglines, SEO) |
| LLM — chatbots | Groq `deepseek-r1-distill-llama-70b` (`<think>` tags stripped) |
| Embeddings | `sentence-transformers/all-MiniLM-L6-v2` (384-D, local HF) |
| Vector DB | Pinecone — indexes `chatbot1` (medical), `chatbot2` (marketing) |
| RAG | LangChain (community/groq/pinecone/openai/experimental) |
| Config | `python-dotenv` (`ml/.env`) |
| Present but unused | `OPENAI_API_KEY`, `REPLICATE_API_TOKEN`, `langchain-openai`, `pandas`, `pypdf` |

---

## 3. Repo Map (meaningful files; ignore `node_modules`, `__pycache__`, any `.venv`)

```
Luminary-Ai/
├── README.md                 # Setup guide — ⚠️ backend run cmd is WRONG (says main:app)
├── CLAUDE.md                 # ← this file (consolidated context)
├── ChangesNeeded.md          # prioritized fixes / changes for the current version
├── ROADMAP.md                # (leftover gen artifact — folded into ChangesNeeded.md)
├── PromptForContextGathering.md  # (leftover meta-prompt to regenerate docs)
│
├── frontend/                 # Next.js 15 app
│   └── src/
│       ├── app/              # App Router pages
│       │   ├── page.tsx          # Home (Navbar, Hero, Work, Sponsors, Footer)
│       │   ├── build/page.tsx    # SEO + tagline generator (StartForm)
│       │   ├── chat/page.tsx     # Full-page chatbot (Chatbot)
│       │   ├── explore/page.tsx  # Company research (CompanyInput + ChatbotSmall)
│       │   ├── sectors/page.tsx  # Agent showcase (ChatbotCard)
│       │   ├── signin|signup/    # Firebase auth pages
│       │   ├── contact|team|sponsors|test/
│       │   ├── layout.tsx        # Root layout, Geist font
│       │   └── globals.css
│       ├── components/       # Feature + UI components
│       │   ├── Analysis.tsx        → POST /companies-analysis (SWOT)
│       │   ├── CompanyInput.tsx    → GET /company
│       │   ├── Chatbot.tsx         → POST /medical-bot (RAG chat, full page)
│       │   ├── ChatbotSmall.tsx    → POST /marketing-bot (floating widget, 600px)
│       │   ├── StartForm.tsx       → GET /seo + POST /tagline-generator
│       │   ├── SWOTAnaylis.tsx     # SWOT display (NOTE: filename typo, missing 'y')
│       │   ├── ChatbotCard.tsx, MultiStepLoader.tsx, Hero.tsx, Navbar.tsx,
│       │   │   Footer.tsx, Work.tsx, Sponsors.tsx, Signin.tsx, Signup.tsx,
│       │   │   ContactUs.tsx, Team.tsx, DottedText.tsx, ScrollButton.tsx …
│       │   └── ui/                 # shadcn primitives (button, card, input, label, alert, scroll-area)
│       ├── hooks/sendMail.tsx      # server action → lib/mail.ts (to mjgandhi2305@gmail.com)
│       └── lib/
│           ├── firebase.ts         # auth + Google/GitHub providers (NEXT_PUBLIC_* vars)
│           ├── mail.ts             # Nodemailer Gmail SMTP
│           ├── templates/welcome.ts
│           └── utils.ts            # cn() Tailwind merge
│
└── ml/                       # FastAPI backend (entry: server.py — NOT main.py)
    ├── server.py             # App, CORS(*), /api/home, /company, /companies-analysis; mounts routers
    ├── config.py             # loads GROQ_API_KEY from env
    ├── companies.py          # get_company_info() — company + 5 competitors (Groq)
    ├── analysis.py           # companies_analysis() — SWOT for first 3 companies (Groq)
    ├── requirements.txt      # unpinned deps (+ duplicate langchain-pinecone)
    ├── 1.ipynb, companies.ipynb   # dev/scratch notebooks (not part of the app)
    ├── routes/
    │   ├── chat_routes.py            # POST /medical-bot
    │   ├── marketing_chatbot_routes.py # POST /marketing-bot
    │   ├── generate_taglines.py      # POST /tagline-generator
    │   └── seo_routes.py             # GET  /seo
    ├── services/
    │   ├── chat_service.py           # RAG: Pinecone chatbot1 + Groq deepseek; strips <think>
    │   ├── marketing_chatbot_service.py # RAG: Pinecone chatbot2
    │   ├── generate_taglines.py
    │   ├── seo_service.py            # get_company_info → 10 SEO keywords
    │   └── model.pkl                 # shipped pickle (provenance UNKNOWN)
    └── chat/src/
        ├── helper.py                 # download_hugging_face_embeddings()
        └── prompt.py                 # system prompts (medical + marketing)
```

> ⚠️ **There is no `.gitignore`** in the repo as of writing (a root one was just added — see
> ChangesNeeded "Already done"). `ml/.env`, virtualenvs, and `__pycache__` were committed in
> the past; they are no longer in the working tree but **the leaked keys remain in git
> history**. See ChangesNeeded §A.

---

## 4. Architecture & Data Flow

```
Browser (Next.js, :3000)
   │  fetch() → hardcoded https://dotslash-backend.onrender.com  (or :8000 locally)
   ▼
FastAPI (ml/server.py, :8000)
   ├─ GET  /api/home          → inline {message, team}
   ├─ GET  /company           → companies.get_company_info()   → Groq llama-3.3-70b
   ├─ POST /companies-analysis→ analysis.companies_analysis()  → Groq llama-3.3-70b (SWOT, first 3)
   ├─ POST /medical-bot       → chat_service                   → RAG: Pinecone(chatbot1)
   │                                                              + HF embeddings + Groq deepseek
   ├─ POST /marketing-bot     → marketing_chatbot_service      → RAG: Pinecone(chatbot2)
   ├─ POST /tagline-generator → services.generate_taglines     → Groq
   └─ GET  /seo               → services.seo_service           → Groq

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
| GET | `/api/home` | — | inline | Health/hello + team names `['Vatsal','Miten','Laskhit']` |
| GET | `/company` | `?company`, `?location` | `companies.get_company_info` | Company + 5 competitors JSON. **Bare `except` returns `{error: str(e)}` with HTTP 200** |
| POST | `/companies-analysis` | JSON body (company info) | `analysis.companies_analysis` | SWOT for **first 3** companies; raises `HTTPException(400)` on error |
| POST | `/medical-bot` | `{ "msg": str }` | `chat_service.get_chat_response` | RAG over Pinecone `chatbot1` (medical) |
| POST | `/marketing-bot` | `{ "msg": str }` | `marketing_chatbot_service` | RAG over Pinecone `chatbot2` (marketing) |
| POST | `/tagline-generator` | `{ company_description, company_sector }` | `services.generate_taglines` | 5 names + taglines |
| GET | `/seo` | `?company_description`, `?location` | `services.seo_service.get_seo` | 10 SEO keywords |

No API versioning, no pagination, **no auth, no rate limiting, no input length limits**.
Swagger UI auto-available at `/docs`.

---

## 6. Backend Component Notes (current behavior)

- **`server.py`** — CORS `allow_origins=["*"]` + `allow_credentials=True` (invalid combo; browsers
  reject). No auth/rate-limit/logging middleware. No real health check.
- **`companies.py` `get_company_info(name, location, api_key)`** — Groq `llama-3.3-70b`, temp 0.3,
  max_tokens 1000. Prompts for structured JSON (official_name, industry_type, headquarters,
  key_products_services[], website, competitors[5]). LLM knowledge only; no web search; no retry.
  JSON parsed by regex-stripping ```` ```json ```` fences → fragile.
- **`analysis.py` `companies_analysis(company_info, api_key)`** — top 3 companies → Groq → SWOT
  per company. Ungrounded; same fragile JSON parsing.
- **`services/chat_service.py`** (medical RAG) — HF `all-MiniLM-L6-v2` (384-D) → Pinecone `chatbot1`,
  `k=3` → LangChain RetrievalQA → Groq `deepseek-r1-distill-llama-70b` → strip `<think>`. System
  prompt: answer only from context, ≤3 sentences. **Re-initializes embeddings + index on EVERY
  request** (slow/wasteful). Knowledge-base PDFs are NOT in the repo; index must pre-exist.
- **`services/marketing_chatbot_service.py`** — identical to medical but Pinecone `chatbot2`,
  `system_prompt2`.
- **`services/seo_service.py` `get_seo(desc, location)`** — calls `get_company_info` then extracts
  10 SEO keywords/company. LLM only; no Google Trends/web data.
- **`services/generate_taglines.py`** — Groq `llama-3.3-70b` → exactly 5 `{name, TagLine}`.

---

## 7. Environment Variables

**Backend (`ml/.env`, via `python-dotenv`)**
| Var | Used in | Purpose |
|---|---|---|
| `GROQ_API_KEY` | `config.py`, services | Groq LLM calls (required) |
| `PINECONE_API_KEY` | chat services | Pinecone vector store |
| `HUGGINGFACEHUB_API_TOKEN` | embeddings | HF embeddings |
| `OPENAI_API_KEY` | — | present in `.env`, **appears unused** |
| `REPLICATE_API_TOKEN` | — | present in `.env`, **appears unused** |

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
# (recommended, not yet used) NEXT_PUBLIC_API_URL=http://localhost:8000
```

> 🔴 **Security:** real keys (Pinecone, OpenAI, HuggingFace, Groq, Replicate) were committed in
> `ml/.env` in earlier commits and **still live in git history**. Rotate all + scrub history.
> See ChangesNeeded §A.

---

## 8. How to Run (corrected)

**Frontend**
```bash
cd frontend
npm install
npm run dev        # http://localhost:3000  (uses --turbopack)
```

**Backend**
```bash
cd ml
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
# Create ml/.env with GROQ_API_KEY (+ PINECONE_API_KEY, HUGGINGFACEHUB_API_TOKEN)
uvicorn server:app --host 0.0.0.0 --port 8000 --reload   # NOT main:app
```

> ⚠️ README says `uvicorn main:app` — **wrong**, there is no `main.py`; the entry is `server.py`.
> ⚠️ The frontend hardcodes the Render URL, so a local backend isn't hit unless you change those
> URLs (ChangesNeeded #5). No test suite, no CI.
> ⚠️ RAG chatbots need pre-populated Pinecone indexes (`chatbot1`, `chatbot2`); no ingestion
> script ships in the repo.

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

---

## 12. Known Issues → see [ChangesNeeded.md](ChangesNeeded.md)

Top risks (full detail + fixes in ChangesNeeded.md):
1. 🔴 **Leaked API keys in git history** (`ml/.env`) — rotate all + scrub history.
2. 🟠 **CORS** `*` + credentials — invalid/insecure.
3. 🟠 **No auth/rate-limit** on paid LLM endpoints — cost & abuse risk.
4. 🟠 **Hardcoded backend URL** across frontend — not configurable.
5. 🟠 **Unpinned Python deps** (+ duplicate line) — non-reproducible builds.
6. 🟡 **Bare `except`** leaking errors; **fragile LLM JSON parsing**; **RAG re-init per request**.
7. ❌ Missing: `/dashboard` + route guards, live web search, conversation memory, tests/CI/Docker, observability.
```
