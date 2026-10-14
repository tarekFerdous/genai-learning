# Misconception: retrieval happens after the LLM call

In lesson 0001 free recall, the user ordered the query path as `embed > call llm > similarity chunks > write output`, putting the LLM before similarity search. Indexing order was correct. Model-call basics: 2/2. Warm-up RAG quiz: 2/4.

**Evidence**: free-recall answer, session 2. Correction given in chat (retrieval is plain code before the call; chunks go into the prompt).

**Implications**: lesson 0002+ must make the user *write* retrieve → stuff prompt → invoke by hand (no chain/agent abstraction hiding the order) before introducing LangChain retrievers or agentic RAG. Also stress that chunk text is stored next to vectors.
