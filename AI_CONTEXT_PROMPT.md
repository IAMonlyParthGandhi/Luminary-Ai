# The One Prompt for Luminary AI

This is a single, ready-to-paste prompt tailored to **this exact repository**
(`Luminary-Ai` = Next.js 15 frontend + FastAPI `ml` backend with Groq/Pinecone/LangChain).

**Why this exists:** Reading the whole codebase by hand is slow, and pasting raw
code into Claude/ChatGPT burns tokens and hits limits. This prompt makes Claude Code
read the repo *once* and produce a small set of dense, reusable documents. After that,
you only ever paste those `.md` files into any AI — cheap, fast, and complete.

---

## How to use it

1. Open a terminal in the repo root (`Luminary-Ai/`).
2. Start Claude Code:
   ```bash
   claude
   ```
3. Copy **everything inside the code block below** and paste it as your first message.
4. Let it run. It will create the docs in a `/docs` folder and a root `CLAUDE.md`.
5. From then on, for any future question to any AI, just paste `CLAUDE.md`
   (and the relevant focused doc) instead of source code.

---

## THE PROMPT (copy everything below)

```
You are onboarding onto a real, existing repository called "Luminary AI". Do NOT
assume — read the actual files before writing anything. This is a monorepo with two
parts:

- frontend/  -> Next.js 15 (App Router, React 19, Turbopack), TypeScript, Tailwind +
   shadcn/ui, Firebase (auth), Nodemailer + Handlebars (contact email), framer-motion.
- ml/        -> FastAPI backend. Entry point is server.py (NOT main.py). Uses Groq
   LLMs, Pinecone vector store, LangChain RAG, sentence-transformers embeddings, and
   ships a services/model.pkl. Routers live in ml/routes/, logic in ml/services/.

GROUND RULES
1. Read before you write. Inspect frontend/src and all of ml/ EXCEPT ml/.venv and any
   __pycache__ / node_modules — ignore those entirely; they are vendored noise.
2. Be precise and cite real file paths and line numbers. If something is unknown or
   ambiguous, write "UNKNOWN — needs owner input" rather than inventing it.
3. Optimize every document for being pasted into another AI later: dense, structured,
   no filler, no repetition. Token-efficiency is the whole point.
4. This is a documentation + audit task. Do NOT change application code or fix bugs in
   this run. Only create the markdown files described below.

PRODUCE THESE FILES

=== 1) CLAUDE.md (root) — the master context pack ===
The single file I can hand to any AI to fully explain the project. Keep it tight.
Include:
- One-paragraph elevator pitch (it's an "AI-as-a-service for small/mid businesses"
  platform: competitor/SWOT analysis, AI branding/taglines, domain chatbots, SEO).
- Tech stack table (frontend vs backend), with exact versions from package.json and
  ml/requirements.txt.
- Repo map: a tree of the meaningful files only (skip .venv/__pycache__/node_modules)
  with a one-line purpose for each folder and each key file.
- Architecture: how frontend pages call backend endpoints; the RAG/LLM data flow
  (Groq + Pinecone + embeddings); where Firebase and Nodemailer fit.
- Endpoint inventory: for every FastAPI route across server.py and ml/routes/*
  (/api/home, /company, /companies-analysis, /medical-bot, marketing chatbot,
  generate taglines, SEO), list method, path, request shape, response shape, and the
  service function it calls.
- Environment variables: every env var actually referenced in code (e.g. GROQ_API_KEY,
  PINECONE_API_KEY, OPENAI_API_KEY, HUGGINGFACEHUB_API_TOKEN, REPLICATE_API_TOKEN, plus
  any Firebase/SMTP vars in the frontend). For each: what it's for and where it's read.
- How to run (corrected): frontend (npm install / npm run dev on :3000) and backend.
  IMPORTANT: verify the real uvicorn command — the README says `uvicorn main:app` but
  the entry file is server.py, so the correct command is `uvicorn server:app`. Call out
  this discrepancy.
- "Status at a glance": for each major feature, mark WORKING / PARTIAL / BROKEN / UNKNOWN
  based on what the code actually supports, with a one-line reason.

=== 2) docs/HEALTH_CHECK.md — what works vs what doesn't ===
Sections: Working Well, Problems/Bugs, Incomplete/Stubbed, Urgent, Nice-to-Have, and
"Top 5 things to do next" (ranked, each with effort estimate S/M/L and impact).

=== 3) docs/ISSUES_AND_FIXES.md — concrete audit ===
A prioritized table of concrete issues with severity (CRITICAL/HIGH/MED/LOW), the file
path, why it matters, and the recommended fix. Specifically verify and report on these
suspected issues (confirm or refute each against the code — do not assume I'm right):
- ml/.env appears to be committed to git with live API keys (Pinecone/OpenAI/HuggingFace/
  Groq/Replicate). If true, this is CRITICAL: list exactly which keys are exposed, and
  give the remediation steps (git rm --cached, rotate every key, add to .gitignore,
  scrub history). Do NOT print the secret values in any document.
- ml/.venv/ and __pycache__ are committed despite being in ml/.gitignore (repo bloat /
  they were tracked before being ignored). Recommend git rm -r --cached.
- CORS in server.py uses allow_origins=["*"] together with allow_credentials=True,
  which is invalid/insecure. Recommend a correct configuration.
- Broad `except Exception` blocks (e.g. server.py /company) that swallow errors and
  return raw error strings to the client — flag info-leak + poor error handling.
- Missing input validation, missing rate limiting, no auth on the AI endpoints (cost/
  abuse risk given paid LLM calls), and any hardcoded values/index names (e.g. the
  Pinecone index "chatbot1").
- Frontend: confirm how the API base URL is configured and whether it's hardcoded to
  localhost (deployment risk).

=== 4) docs/ROADMAP.md — what to build next ===
- Completed features (verified from code).
- Gaps and missing standard features for a platform like this (auth/session handling,
  persistence/DB — note there is currently no database, payment/usage metering, tests,
  CI, error monitoring, dockerization).
- Phased plan: Phase 1 (security + correctness, blocking), Phase 2 (UX + reliability),
  Phase 3 (scale + polish). Each item: short rationale + S/M/L effort.

OUTPUT RULES
- Create CLAUDE.md in the repo root and the rest under docs/.
- Use real, verified details from the code. Where you couldn't verify, say so explicitly.
- After writing the files, reply in chat with a 10-line summary: the 3 most urgent
  problems, and exactly which one file I should paste into an AI next time to get help
  on (a) security, (b) a new feature.
```

---

## After it finishes

- For day-to-day AI help, paste **`CLAUDE.md`** only. It's built to be the whole-project
  context in the fewest tokens.
- For a focused task, also paste the one matching doc (`ISSUES_AND_FIXES.md`,
  `ROADMAP.md`, etc.).
- Re-run the prompt whenever the project changes significantly to refresh the docs.

> Tip: the single most important fix this prompt will surface is that **`ml/.env` with
> live API keys is committed to the repo** — rotate those keys regardless of anything
> else.
