# Re-Reading Is Not Free: Token Traces and Cache-Aware Energy Estimation for LLM Agents in Software Engineering

- arXiv ID: `2611.20873v1`
- Authors: Tina Vartziotis, Ketevan Peranidze, Rodopi Kosteli, Ezgi Sarikayak, George Dasoulas, Michael Keckeisen, Sotirios Kotsopoulos, Francesca Dominici
- Published: 2026-11-16
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2611.20873v1) | [pdf](https://arxiv.org/pdf/2611.20873v1)

## Abstract

As large language models (LLMs) evolve from conversational assistants into autonomous agents embedded in software development workflows, estimating their environmental footprint requires moving beyond conventional token-based accounting. Existing energy estimators focus on isolated request-response interactions, overlooking the repeated processing of accumulated context, cache reuse, and work delegated to subagents. We analyze nearly one billion tokens collected across 42 sessions and 752 task episodes over ten weeks of real-world AI-assisted software development. Cached-context reads make up 94.8% of all API-reported tokens, while uncached input accounts for only 0.017%; for every generated token, approximately 260 cached tokens are read. Context grows 5.3-fold over a session compared with 1.4-fold within individual tasks. To quantify the energy implications, we extend an existing analytical inference-energy model to account for cached-context processing, yielding a cache-aware hybrid estimator. It estimates approximately 250 kWh for the workload, compared with approximately 10 kWh from the output-based estimator EcoLogits, a 25-fold difference largely driven by cached-context reads. Neither estimator has been validated on long cached contexts, but no modeling assumption we varied closes the gap. Starting each task from a fresh context would lower our estimate by about 60%. We also find that parent-session logs report only a subagent's final internal call, undercounting delegated tokens by a factor of ten; for this workload the correction changes the energy estimate by about 5%, but token-volume studies are fully exposed to it. Our findings expose a substantial gap between how current energy estimators and agentic workloads treat context, highlighting the need for workflow-level energy accounting that captures context accumulation, cache reuse, and delegated execution.
