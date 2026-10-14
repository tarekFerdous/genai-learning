# GenAI Glossary

Canonical terms for this workspace. A term is added only once the learner has used it correctly.

## Model calls

**Chat model**:
A model that takes a list of messages and returns one message; stateless between calls.
_Avoid_: LLM chain, bot

**Message**:
One turn in a chat model's input/output: `SystemMessage` (rules + context), `HumanMessage` (user), `AIMessage` (model reply with `content` and `usage_metadata`).
_Avoid_: prompt string (a prompt is the whole message list)

**Temperature**:
Sampling randomness; 0 gives near-repeatable outputs, higher gives more varied ones.

**Streaming**:
Receiving a reply token-by-token as it is generated, cutting time-to-first-token, not total time.

## RAG

**Indexing**:
The offline phase: load → chunk → embed → store text with its vector.
_Avoid_: training (the model is never changed)

**Embedding**:
A fixed-length vector of numbers representing a text's meaning; only comparable with vectors from the same embedding model.
_Avoid_: encoding, vectorised text

**Cosine similarity**:
The angle-based score between two embeddings: ~1 same meaning, ~0 unrelated. Scores are relative; compare ranks, not absolutes.

**Retrieval**:
The query-time step that embeds the question and returns the top-k most similar chunks. Plain code that runs *before* the chat model is called.
_Avoid_: search (too vague: keyword vs semantic matters)

**Grounding**:
Constraining the chat model to answer only from the retrieved context, and to refuse when it isn't there. Answer quality is capped by retrieval quality.
