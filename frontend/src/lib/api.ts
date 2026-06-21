// Single source of truth for the backend base URL.
// Override per environment with NEXT_PUBLIC_API_URL (e.g. the Render URL in prod).
export const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";
