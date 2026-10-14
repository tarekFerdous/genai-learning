# GenAI / RAG / LangGraph Resources

Versions checked 2026-10-14: `langchain` 1.4.5 (Python ≥3.10), `langgraph` 1.2.15. Prefer docs for v1+; many blogs/videos still show pre-v1 APIs (`langchain.chains`, `create_react_agent`).

## Knowledge

- [LangChain docs: Models](https://docs.langchain.com/oss/python/langchain/models)
  `init_chat_model`, invoke/stream/batch, provider config. Use for: any model-call question.
- [LangChain v1 migration guide](https://docs.langchain.com/oss/python/migrate/langchain-v1)
  What changed in v1 (`create_agent`, `system_prompt`, moved imports). Use for: translating old tutorials/videos to current APIs.
- [LangChain docs: RAG tutorial](https://docs.langchain.com/oss/python/langchain/rag)
  Official end-to-end retrieval build incl. splitter/embeddings/vector store choices and prompt-injection warning. Use for: indexing + agentic retrieval.
- [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview)
  Stateful graphs, persistence, interrupts, memory. Use for: everything LangGraph.
- [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence) and [interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)
  Checkpointers, threads, human-in-the-loop. Use for: memory + approval flows in the capstone.
- [API reference: langchain.agents](https://reference.langchain.com/python/langchain/agents)
  Exact signatures. Use for: when docs prose is ambiguous.
- [Anthropic: Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval)
  Primary-source study of contextual embeddings + BM25 hybrid + reranking with measured failure-rate reductions. Use for: retrieval-quality upgrades.
- [Ragas docs](https://docs.ragas.io)
  Faithfulness, context precision/recall, answer relevancy. Note 0.4.x moved metrics to `ragas.metrics.collections`. Use for: eval harness.
- [Hamel Husain: Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/)
  Practitioner guide to eval-driven development. Use for: designing the eval loop, not trusting vibes.
- Book: _AI Engineering_ by Chip Huyen (O'Reilly, 2025)
  The field's reference text on building on foundation models (RAG, agents, evals, inference cost). Use for: depth on any production topic.
- [Ollama docs](https://docs.ollama.com)
  Running local models + embeddings. Use for: local dev setup.
- [LangSmith tracing quickstart](https://docs.langchain.com/langsmith/trace-with-langchain)
  Observability for chains/graphs. Use for: debugging + production monitoring.

## Wisdom (Communities)

- [LangChain Forum](https://forum.langchain.com)
  Official Q&A, maintainers answer. Use for: framework-specific bugs and design questions.
- [r/LocalLLaMA](https://reddit.com/r/LocalLLaMA)
  Largest local-model community. Use for: which local model/quant fits 16 GB, tool-calling reliability reports.
- [MLOps Community](https://mlops.community)
  Practitioner Slack + talks on shipping ML/LLM systems. Use for: portfolio feedback, production war stories, job leads.

## Gaps
- No verified benchmark of local-model tool-calling reliability on 16 GB VRAM; test ourselves.
- Capstone domain not chosen yet → domain-specific sources TBD.
