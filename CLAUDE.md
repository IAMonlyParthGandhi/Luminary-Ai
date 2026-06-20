# CLAUDE.md — Luminary AI Master Context Pack

> **Purpose of this file:** This is the single document to paste into any AI (Claude,
> GPT, etc.) to give it full context on this project in the fewest tokens. It replaces
> pasting source code. Keep it updated when architecture changes.
> Last generated from code on: **2026-06-20**.

---

## 1. Elevator Pitch

**Luminary AI** is an *AI-as-a-service platform for small and mid-sized businesses*. It
provides AI-driven business tooling: competitor discovery + **SWOT analysis**, AI
**branding/tagline generation**, **domain-specific chatbots** (RAG), and **SEO**
content help. It's a two-part monorepo: a **Next.js** marketing/app frontend and a
**FastAPI** backend that wraps **Groq** LLMs, a **Pinecone** vector store, and
**LangChain** RAG pipelines.

> Note: the team also refers to the backend as "DotSlash" — the deployed backend lives
> at `https://dotslash-backend.onrender.com` (hardcoded in the frontend, see Issues).

---

## 2. Tech Stack

| Layer | Tech | Version (from manifests) |
|---|---|---|
| Frontend framework | Next.js (App Router) + React | `next 15.1.6`, `react 19.0.0` |
| Language | TypeScript | `^5` |
| Styling | Tailwind CSS + shadcn/ui + Radix | `tailwindcss 3.4.1` |
| Animation | framer-motion | `^12.0.6` |
| Auth (client) | Firebase Auth (Google + GitHub providers) | `firebase ^11.2.0` |
| Email | Nodemailer + Handlebars | `nodemailer ^6.10.0` |
| Markdown render | react-markdown | `^9.0.3` |
| Backend framework | FastAPI (`fastapi[all]`) | unpinned |
| LLM provider | Groq (`llama-3.3-70b-versatile`, `deepseek-r1-distill-llama-70b`) | unpinned |
| Vector DB | Pinecone (index `chatbot1`) | unpinned |
| RAG orchestration | LangChain (community/groq/pinecone/openai/experimental) | unpinned |
| Embeddings | sentence-transformers (HuggingFace) | unpinned |
| Other | pandas, pypdf, replicate (token referenced) | unpinned |

> ⚠️ All Python deps in `ml/requirements.txt` are **unpinned** (no `==`), so builds are
> non-reproducible. See `docs/ISSUES_AND_FIXES.md`.

---

## 3. Repo Map (meaningful files only — ignore `ml/.venv`, `__pycache__`, `node_modules`)

```
Luminary-Ai/
├── README.md                 # Setup guide (NOTE: backend run cmd is wrong — see §6)
├── AI_CONTEXT_PROMPT.md      # Reusable prompt to regenerate these docs
├── CLAUDE.md                 # ← this file
├── docs/
│   ├── HEALTH_CHECK.md       # What works / what doesn't
│   ├── ISSUES_AND_FIXES.md   # Prioritized audit + fixes
│   └── ROADMAP.md            # What to build next
│
├── frontend/                 # Next.js 15 app
│   └── src/
│       ├── app/              # App Router pages
│       │   ├── page.tsx          # Home (Hero, Work, Sponsors, ContactUs)
│       │   ├── build/page.tsx    # "Start a business" flow (StartForm)
│       │   ├── chat/page.tsx     # Chatbot UI
│       │   ├── explore/page.tsx  # Company input → analysis
│       │   ├── sectors/page.tsx
│       │   ├── signin|signup/    # Firebase auth pages
│       │   ├── sponsors|team|contact|test/
│       │   ├── layout.tsx        # Root layout
│       │   └── globals.css
│       ├── components/       # Feature + UI components
│       │   ├── Analysis.tsx      # → POST /companies-analysis (SWOT)
│       │   ├── CompanyInput.tsx  # → GET /company
│       │   ├── Chatbot.tsx       # → POST /medical-bot (RAG chat)
│       │   ├── ChatbotSmall.tsx  # → POST /marketing-bot
│       │   ├── StartForm.tsx     # → GET /seo, POST /tagline-generator
│       │   ├── SWOTAnaylis.tsx, MultiStepLoader.tsx, Hero.tsx, Navbar.tsx, Footer.tsx …
│       │   └── ui/               # shadcn primitives (button, card, input, …)
│       ├── hooks/sendMail.tsx
│       └── lib/
│           ├── firebase.ts       # Firebase init (NEXT_PUBLIC_* env vars)
│           ├── mail.ts           # Nodemailer transport
│           ├── templates/welcome.ts
│           └── utils.ts
│
└── ml/                       # FastAPI backend (entry: server.py)
    ├── server.py             # App, CORS, /api/home, /company, /companies-analysis; mounts routers
    ├── config.py             # Loads GROQ_API_KEY from env
    ├── companies.py          # get_company_info() — company + competitors (Groq)
    ├── analysis.py           # companies_analysis() — SWOT for first 3 companies (Groq)
    ├── requirements.txt      # (unpinned deps)
    ├── .env                  # ⚠️ COMMITTED WITH LIVE KEYS — see Issues (CRITICAL)
    ├── routes/
    │   ├── chat_routes.py            # POST /medical-bot
    │   ├── marketing_chatbot_routes.py # POST /marketing-bot
    │   ├── generate_taglines.py      # POST /tagline-generator
    │   └── seo_routes.py             # GET  /seo
    ├── services/
    │   ├── chat_service.py           # RAG: Pinecone "chatbot1" + Groq deepseek; strips <think>
    │   ├── marketing_chatbot_service.py
    │   ├── generate_taglines.py
    │   ├── seo_service.py
    │   └── model.pkl                 # shipped pickle (provenance UNKNOWN)
    └── chat/
        ├── src/helper.py             # download_hugging_face_embeddings()
        └── src/prompt.py             # system prompts
```

---

## 4. Architecture & Data Flow

```
Browser (Next.js, :3000)
   │  fetch() to hardcoded https://dotslash-backend.onrender.com  (or :8000 locally)
   ▼
FastAPI (ml/server.py, :8000)
   ├─ /company            → companies.get_company_info()      → Groq llama-3.3-70b
   ├─ /companies-analysis → analysis.companies_analysis()     → Groq llama-3.3-70b (SWOT)
   ├─ /medical-bot        → chat_service.get_chat_response()  → RAG: Pinecone(chatbot1)
   │                                                              + HF embeddings
   │                                                              + Groq deepseek-r1-70b
   ├─ /marketing-bot      → marketing_chatbot_service
   ├─ /tagline-generator  → services.generate_taglines (Groq)
   └─ /seo                → services.seo_service (Groq)

Firebase Auth (client-side only): Google + GitHub sign-in. No backend session/JWT verify.
Email: frontend lib/mail.ts (Nodemailer + Handlebars welcome template) for contact form.
```

**Key characteristics:**
- **No database.** All "data" is generated on-the-fly by LLM calls. Pinecone holds only
  the chatbot's vector index. No user/session/business records are persisted.
- **Auth and backend are disconnected.** Firebase auth happens in the browser; the
  FastAPI endpoints do **not** verify any token — every AI endpoint is publicly callable.
- **RAG chatbot** (`/medical-bot`) retrieves top-3 chunks from Pinecone index `chatbot1`
  and answers with Groq; `<think>...</think>` reasoning is stripped from the reply.

---

## 5. Endpoint Inventory

| Method | Path | Request | Calls | Notes |
|---|---|---|---|---|
| GET | `/api/home` | — | inline | Health/hello + team names |
| GET | `/company` | query: `company`, `location` | `companies.get_company_info` | Returns company + competitors JSON. Bare `except` returns `{error}` |
| POST | `/companies-analysis` | JSON body (company info) | `analysis.companies_analysis` | SWOT for **first 3** companies; raises 400 on error |
| POST | `/medical-bot` | `{ "msg": str }` | `chat_service.get_chat_response` | RAG over Pinecone `chatbot1` |
| POST | `/marketing-bot` | `{ "msg": str }` | `marketing_chatbot_service.get_chat_response` | Marketing chatbot |
| POST | `/tagline-generator` | `{ "company_description": str, "company_sector": str }` | `services.generate_taglines.get_company_info` | Branding taglines |
| GET | `/seo` | query: `company_description`, `location` | `services.seo_service.get_seo` | SEO suggestions |

All responses are JSON. There is **no API versioning**, **no pagination**, **no auth**,
and **no rate limiting**.

---

## 6. Environment Variables

**Backend (`ml/`)** — read via `python-dotenv`:

| Var | Used in | Purpose |
|---|---|---|
| `GROQ_API_KEY` | `config.py`, services | Groq LLM calls (required) |
| `PINECONE_API_KEY` | `chat_service.py` | Pinecone vector store |
| `OPENAI_API_KEY` | `.env` (langchain-openai dep) | Present; verify if actually used |
| `HUGGINGFACEHUB_API_TOKEN` | `.env` / embeddings | HF embeddings download |
| `REPLICATE_API_TOKEN` | `.env` | Present; verify if actually used |

**Frontend (`frontend/`)** — `NEXT_PUBLIC_*` (client-exposed), read in `lib/firebase.ts`:
`NEXT_PUBLIC_FIREBASE_API_KEY`, `_AUTH_DOMAIN`, `_PROJECT_ID`, `_STORAGE_BUCKET`,
`_MESSAGING_SENDER_ID`, `_APP_ID`. Email (`lib/mail.ts`) likely needs SMTP vars —
**verify** which (`SMTP_HOST/USER/PASS` or similar).

> 🔴 **CRITICAL:** `ml/.env` is **committed to git with real keys** (Pinecone, OpenAI,
> HuggingFace, Groq, Replicate). Rotate all of them and untrack the file. See
> `docs/ISSUES_AND_FIXES.md` #1.

---

## 7. How to Run (corrected)

**Frontend:**
```bash
cd frontend
npm install
npm run dev        # http://localhost:3000  (uses --turbopack)
```

**Backend:**
```bash
cd ml
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
# Create ml/.env with GROQ_API_KEY=... (and PINECONE_API_KEY, HUGGINGFACEHUB_API_TOKEN)
uvicorn server:app --host 0.0.0.0 --port 8000 --reload
```

> ⚠️ **README is wrong.** It says `uvicorn main:app`. There is no `main.py`; the entry
> module is `server.py`, so the correct command is **`uvicorn server:app`**.

> ⚠️ The frontend calls `https://dotslash-backend.onrender.com` hardcoded in several
> components, so running the backend locally won't be hit unless you change those URLs
> (see Issues #5). There is no test suite and no CI.

---

## 8. Status at a Glance

| Feature | Status | Reason |
|---|---|---|
| Company + competitor lookup (`/company`) | ✅ WORKING | Implemented, Groq-backed |
| SWOT analysis (`/companies-analysis`) | ✅ WORKING | Implemented (limited to 3 companies) |
| RAG chatbot (`/medical-bot`) | ⚠️ PARTIAL | Depends on prebuilt Pinecone index `chatbot1`; var named "medical" suggests reused template |
| Marketing chatbot (`/marketing-bot`) | ⚠️ UNKNOWN | Verify `marketing_chatbot_service` content |
| Tagline generator (`/tagline-generator`) | ✅ WORKING | Implemented |
| SEO (`/seo`) | ⚠️ UNKNOWN | Verify `seo_service` content |
| Firebase auth (frontend) | ⚠️ PARTIAL | Client sign-in only; not enforced on backend |
| Contact email | ⚠️ UNKNOWN | Verify SMTP env config |
| Persistence/DB | ❌ NONE | No database in the project |
| Tests / CI | ❌ NONE | None present |

---

## 9. Top Risks (full detail in `docs/ISSUES_AND_FIXES.md`)

1. 🔴 **Live API keys committed** in `ml/.env` — rotate + untrack immediately.
2. 🔴 **`ml/.venv/` committed** (thousands of vendored files) — bloats repo; untrack.
3. 🟠 **CORS** `allow_origins=["*"]` + `allow_credentials=True` — invalid/insecure combo.
4. 🟠 **No auth/rate-limiting** on paid LLM endpoints — cost & abuse risk.
5. 🟠 **Hardcoded backend URL** scattered across frontend components — no env config.
6. 🟠 **Unpinned Python deps** — non-reproducible builds.
7. 🟡 **Bare `except`** returning raw error strings — info leak + poor UX.
