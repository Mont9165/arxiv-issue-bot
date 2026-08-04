# Don't Offer What Can't Be Done: Deterministic Executability Gating for LLM Skill Selection at Scale

- arXiv ID: `2608.01050v1`
- Authors: Ortal Ashkenazi, Vitalii Kloz, Mykhailo Ulianchenko
- Published: 2026-08-02
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.CL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.01050v1) | [pdf](https://arxiv.org/pdf/2608.01050v1)

## Abstract

Production LLM agents that select from large skill libraries face a limitation that semantic relevance alone cannot resolve: a skill may match a user's topic yet be impossible to execute in the current account state. We present a deployed three-stage selection pipeline for Helpmate, Wix's customer-care assistant. First, a recall-oriented semantic matcher identifies messages related to a ten-skill domain family without consulting account state. Second, a deterministic executability gate removes candidates whose internal hard-stop conditions hold. Because the gate and the skill evaluate the same exit predicates, every blocked candidate would be unable to complete under the same account state, provided predicate parity is preserved and both checks observe fresh authoritative state. Finally, the LLM decides whether to invoke one of the remaining candidates.
  In a post-launch production analysis of 756.6K user messages across 267.6K conversations, semantic matching retained 174,927 messages (23.1%). Within this matched stream, the gate removed 1,039,462 of 1,749,270 skill-message pairs (59.4%), saving 228.8 million skill-description tokens -- 59.1% of the post-semantic skill-description footprint. Together, semantic matching and executability gating reduced skill-description context by 90.5% relative to exposing all ten skills to every message.
  To test whether this pruning affects model behavior rather than context size alone, we replayed a risk-enriched cohort of 1,000 conversations with all ten skills exposed. The model selected a production-blocked skill in 78 conversations (7.8%). This counterfactual result shows that deterministic gating prevents non-executable candidates from influencing model selection, while not claiming downstream tool execution or customer-outcome effects.
