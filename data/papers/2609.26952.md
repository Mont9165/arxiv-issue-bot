# Escaping Python Dependency Hell: A Hybrid Replay-and-Repair Pipeline for Python Dependency Resolution

- arXiv ID: `2609.26952v1`
- Authors: Veronica Poweska, Ariana Oyanguren, Jessica Pourleyli, Sourena Khanzadeh, Manar Alalfi
- Published: 2026-09-22
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.MA`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.26952v1) | [pdf](https://arxiv.org/pdf/2609.26952v1)

## Abstract

Dependency conflicts in Python ecosystems arise from incompatible version constraints, missing packages, and undocumented compatibility relationships, causing many real-world code snippets to fail at execution. This paper presents PLLM+, a hybrid dependency-repair pipeline evaluated on the HG2.9K benchmark of 2,891 dependency-failing snippets. PLLM+ prioritizes inexpensive deterministic steps before invoking LLM-based repair: static AST-based interpreter inference, replay of historically successful dependency configurations from the competition-provided solutions database, and live PyPI validation of candidate package versions. When these steps do not resolve a case, the system falls back to a structured LLM-based repair loop with typed error classification and Proposer/Critic agents. On HG2.9K, PLLM+ solves 1,500 out of 2,891 snippets, compared with 1,169 solved by the PLLM baseline. It also reduces average runtime from 368.7 to 71.8 seconds per snippet. Most successful fixes come from replaying known configurations: 1,495 of the 1,500 successful fixes are produced by the solutions database, while the LLM fallback accounts for 5 additional fixes. These results suggest that, in this benchmark setting, deterministic reuse of previously validated dependency configurations is a simple and effective strategy, with LLM-based repair serving as a secondary fallback for cases not covered by prior solutions.
