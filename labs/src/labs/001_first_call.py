from langchain.chat_models import init_chat_model
from langchain.messages import SystemMessage, HumanMessage

model = init_chat_model("qwen3:8b", model_provider="ollama", temperature=0)

messages = [
    SystemMessage("You are a concise tutor. Answer in at most two sentences."),
    HumanMessage("What is retrieval-augmented generation?"),
]

response = model.invoke(messages)

for chunk in model.stream(messages):
    print(chunk.content, end="", flush=True)

print(type(response).__name__)
print(response.content)
print(response.usage_metadata)