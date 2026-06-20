# ISSUES_AND_FIXES.md — Luminary AI

> Prioritized, code-verified audit. Generated **2026-06-20**. Severity:
> 🔴 CRITICAL · 🟠 HIGH · 🟡 MEDIUM · ⚪ LOW.

| # | Sev | Issue | Location | Fix |
|---|---|---|---|---|
| 1 | 🔴 | Live API keys committed | `ml/.env` | Rotate ALL keys, untrack, scrub history (below) |
| 2 | 🔴 | Virtualenv committed | `ml/.venv/**`, `ml/__pycache__/` | `git rm -r --cached` (below) |
| 3 | 🟠 | Insecure CORS combo | `ml/server.py:16-22` | Explicit origins; don't pair `*` with credentials |
| 4 | 🟠 | No auth/rate-limit on paid LLM endpoints | all `ml/routes/*` | Add API key/JWT + rate limiting |
| 5 | 🟠 | Hardcoded backend URL duplicated | `Analysis.tsx`, `Chatbot.tsx`, `ChatbotSmall.tsx`, `CompanyInput.tsx`, `StartForm.tsx:53` | Centralize via `NEXT_PUBLIC_API_BASE_URL` |
| 6 | 🟠 | Unpinned Python deps | `ml/requirements.txt` | Pin with `==`; consider lockfile |
| 7 | 🟡 | Bare `except` leaks errors | `ml/server.py:40-43` | Log server-side, return generic message |
| 8 | 🟡 | Fragile LLM JSON parsing | `companies.py:124-131`, `analysis.py:77-84` | Use Groq JSON mode / validate with Pydantic |
| 9 | 🟡 | RAG re-inits per request | `ml/services/chat_service.py:12-41` | Init embeddings/index once at startup |
| 10 | ⚪ | "medical-bot" naming mismatch | `ml/routes/chat_routes.py:10` | Rename route/index to domain |

---

## 1. 🔴 Live API keys committed in `ml/.env`
`ml/.env` is tracked and contains real `PINECONE_API_KEY`, `OPENAI_API_KEY`,
`HUGGINGFACEHUB_API_TOKEN`, `GROQ_API_KEY`, `REPLICATE_API_TOKEN`. Anyone with repo
access (it's a public-style clone) can use them and run up bills.

**Fix (do in order):**
1. **Rotate every key now** in each provider's dashboard — assume all are compromised.
2. Untrack and ignore:
   ```bash
   git rm --cached ml/.env
   echo ".env" >> ml/.gitignore
   git commit -m "Stop tracking ml/.env; rotate leaked keys"
   ```
3. Add `ml/.env.example` with empty placeholders for onboarding.
4. **Scrub history** (keys live in past commits): use `git filter-repo` or BFG, e.g.
   `git filter-repo --path ml/.env --invert-paths`, then force-push (coordinate with team).

## 2. 🔴 `ml/.venv/` and `__pycache__` committed
Thousands of vendored files are tracked even though `ml/.gitignore` lists `.venv` and
`__pycache__` — they were committed before being ignored. This bloats clones and leaks
local paths.
```bash
git rm -r --cached ml/.venv ml/__pycache__ ml/**/__pycache__
git commit -m "Untrack virtualenv and bytecode caches"
```

## 3. 🟠 Insecure CORS — `ml/server.py:16-22`
```python
# current — invalid: browsers reject "*" with credentials
allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
```
```python
# fix
import os
origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")
app.add_middleware(CORSMiddleware,
    allow_origins=origins, allow_credentials=True,
    allow_methods=["GET", "POST"], allow_headers=["*"])
```

## 4. 🟠 No auth / rate limiting on paid endpoints
Every AI route is public; each call spends Groq/Pinecone quota — trivial to abuse.
- Add a shared-secret header or Firebase ID-token verification (`firebase-admin`) as a
  FastAPI dependency on the routers.
- Add rate limiting (e.g. `slowapi`) keyed by IP/API key.

## 5. 🟠 Hardcoded backend URL across the frontend
`https://dotslash-backend.onrender.com` is hardcoded in 4+ components; `StartForm.tsx`
defines its own `const API_BASE_URL`. Inconsistent and unconfigurable.
```ts
// frontend/src/lib/api.ts
export const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";
```
Import it everywhere; add `NEXT_PUBLIC_API_BASE_URL` to `.env.local` / host config.

## 6. 🟠 Unpinned dependencies — `ml/requirements.txt`
All entries lack versions, so installs drift and can break. Pin them
(`pip freeze` from a known-good venv, excluding local paths) or adopt `uv`/`pip-tools`.

## 7. 🟡 Bare `except` leaks errors — `ml/server.py:40-43`
Returns `{"error": str(e)}` (internal detail) with a 200. Log server-side; return a
generic message and proper status code, matching `/companies-analysis` which already
raises `HTTPException(400)`.

## 8. 🟡 Fragile LLM JSON parsing — `companies.py`, `analysis.py`
Regex-stripping fences then `json.loads` throws on any malformed output. Prefer Groq's
JSON response mode and validate with a Pydantic schema; fall back gracefully.

## 9. 🟡 RAG re-initialized every request — `ml/services/chat_service.py`
`download_hugging_face_embeddings()` and `PineconeVectorStore.from_existing_index()` run
on **every** call → slow, wasteful. Initialize once at app startup (FastAPI lifespan)
and reuse the retriever/chain.

## 10. ⚪ "medical-bot" naming — `ml/routes/chat_routes.py`
Route `/medical-bot` and index `chatbot1` look inherited from a medical RAG template.
Rename to the Luminary domain and confirm the indexed corpus is correct.
