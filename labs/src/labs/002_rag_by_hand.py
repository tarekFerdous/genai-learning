import math
from langchain.chat_models import init_chat_model
from langchain.messages import SystemMessage, HumanMessage
from langchain_ollama import OllamaEmbeddings

# Indexing
# Company handbook
chunks = [
    "Acme Robotics employees may work remotely up to 3 days per week; Tuesday is a mandatory office day.",
    "New hires receive a laptop budget of $2,400, refreshed every 3 years.",
    "Expense reports must be filed within 30 days through the Ledgerly portal.",
    "The on-call rotation is one week long and pays a $500 stipend.",
    "Annual leave is 25 days, plus the office closes between Christmas and New Year.",
    "Production deploys are frozen every Friday after 2pm.",
    "The cafeteria serves free lunch Monday to Thursday.",
    "Security incidents must be reported in #sec-incidents within 1 hour.",
]

embedder = OllamaEmbeddings(model="nomic-embed-text")
vectors = embedder.embed_documents(chunks)
print(len(vectors[0]))
# Indexing
index = list(zip(chunks, vectors))

def cosine(a, b):
    dot = sum(x*y for x, y in zip(a, b))
    norms = math.sqrt(sum(x*x for x in a)) * math.sqrt(sum(y*y for y in b))
    return dot/norms

def retrieve(question, k=2):
    q = embedder.embed_query(question)
    scored = [(cosine(q, vec), text) for text, vec in index]
    scored.sort(reverse=True)
    return scored[:k]


question1 = "Can I deploy to production on Friday afternoon?"
question2 = "Is working from home allowed?"
question3 = "What is the CEO's name?'"
hits = retrieve(question3)
for score, text in hits:
    print(f"{score:.3f} {text}")
    
context = "\n".join(f"- {text}" for _, text in hits)
model = init_chat_model("qwen3:8b", model_provider="ollama", temperature=0)
response = model.invoke([
    SystemMessage(
        "Answer using ONLY the context below. "
        "If the answer is not in the context, say \"\"\n\n"
        f"Context:\n{context}"
    ),
    HumanMessage(question3)
])

print("\n", response.content)