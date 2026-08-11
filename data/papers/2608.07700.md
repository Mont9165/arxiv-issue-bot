# Towards Researcher Agents for Knowledge-Graph Question Answering

- arXiv ID: `2608.07700v1`
- Authors: Tommaso Soru, Abdulsobur Oyewale
- Published: 2026-08-07
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.07700v1) | [pdf](https://arxiv.org/pdf/2608.07700v1)

## Abstract

Translating a natural-language question into a SPARQL query that can be executed against a large knowledge graph requires resolving lexical ambiguity, grounding surface terms in the target ontology, and producing graph patterns that are both syntactically valid and semantically faithful. We present an agentic text-to-SPARQL system that goes one step beyond static tool-using agents: a researcher agent that, after each round of inference on a validation set, proposes and tests changes to its own prompts, rules, and tool-orchestration code. We instantiate the loop on DBpedia, evolve nine successive versions of the agent driven by a low-cost reasoning model, and deploy the best-performing configuration with two stronger backbone models. The study yields three observations: (i) self-improvement converges quickly and then achieves 0.22 overall accuracy on the 2025 DBpedia validation set; (ii) the bottleneck is consistently in basic-graph-pattern predicate selection, not in SPARQL syntax or modifiers; and (iii) several benchmark items appear to penalise correct queries due to property ambiguity in DBpedia, suggesting that future Text-to-SPARQL benchmarks should be scored using a combination of machine translation and information retrieval metrics.
