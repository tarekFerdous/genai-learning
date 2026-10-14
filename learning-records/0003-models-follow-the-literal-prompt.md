# Models follow the literal prompt; behaviour must be measured, not assumed

Two findings from lesson 0002. (1) User edited the grounding instruction to `say ""` and the model returned an empty string. The model obeyed the prompt as written, not as intended. (2) With the grounding instruction removed, Qwen3-8B still refused to invent a CEO name, which contradicted the lesson's prediction. Modern models often resist obvious-gap hallucinations; the risky cases are near-misses.

**Evidence**: lesson 0002 exercises c–e; quiz 4/4. Also debugged a broken f-string generator (`"\n".join(f"... for _, text in hits")`) and a silent kwarg typo (`temperatur`).

**Implications**: teach "print the context first" as the reflex for debugging. Use near-miss questions in eval sets (Phase 3). Silent kwarg typos make a case for config objects and type-checked settings later.
