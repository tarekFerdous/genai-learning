# Notes

## Learner preferences
- Learns by doing: watched a 2–4h RAG video (LangChain → LangGraph) but wants hands-on so it sticks. Every lesson must end with code they ran themselves.
- Goal is interview confidence: always include the "why" + trade-off, phrased so they could say it aloud in an interview.
- Python. Windows 11 + PowerShell. Python 3.13, Docker, Ollama installed. `uv` not installed yet (lesson 0001 installs it).
- Iterative: start basic, keep improving the same system toward production grade.

## Provider strategy (agreed default)
- Dev/learning: local Ollama (free, unlimited iteration). Chat: `qwen3:8b` (bump to `qwen3:14b` if quality lacking). Embeddings: local later.
- Deployed capstone: frontier API (deployed server has no GPU; better tool-calling reliability). Cost is cents/day at portfolio traffic.
- Code is provider-agnostic from day one via `init_chat_model` + config.

## Roadmap (draft — adjust via learning records)
Phase 1 Foundations: model calls → prompts + structured output → embeddings & similarity by hand → chunking → vector store → naive RAG end to end.
Phase 2 LangGraph: graphs/state → tools & agents → agentic RAG (route/grade/rewrite) → memory/persistence → human-in-the-loop.
Phase 3 Production: eval set + Ragas → hybrid search + rerank → observability → FastAPI + streaming → Postgres/pgvector → Docker → guardrails/prompt-injection → cost/latency → CI → deploy.
Capstone starts at end of Phase 1 and evolves with each lesson.
