# FuzzAgent: Multi-Agent System for Evolutionary Library Fuzzing

- arXiv ID: `2605.14431v1`
- Authors: Yunlong Lyu, Peng Chen, Fengyi Wu, Junzhe Yu, Kit Long Hon, Hao Chen
- Published: 2026-05-14
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2605.14431v1) | [pdf](https://arxiv.org/pdf/2605.14431v1)

## Abstract

Library fuzzing is essential for hardening the software supply chain, but adopting it at scale remains expensive. Practitioners still spend substantial effort on environment setup, struggle to generate harnesses that respect intricate API constraints, and lack reliable means to tell genuine library bugs from harness-induced crashes. Recent LLM-based systems automate parts of this pipeline, yet they typically operate as one-shot code generators that ignore runtime feedback, which limits both the depth of code they reach and the validity of the bugs they report. We argue that effective library fuzzing is iterative by nature: each campaign exposes new coverage bottlenecks and crashes, and the next campaign should evolve from these signals rather than restart from scratch. Building on this insight, we present FuzzAgent, a multi-agent system that turns library fuzzing into an evolutionary process, in which a team of specialized agents collaborates over the full fuzzing lifecycle and grounds every decision in concrete runtime evidence, so that the harness suite is successively refined toward deeper coverage and higher-fidelity crash analysis across rounds.
  We evaluate FuzzAgent on 20 real-world C/C++ libraries against four state-of-the-art baselines (OSS-Fuzz, OSS-Fuzz-Gen, PromptFuzz, and PromeFuzz). FuzzAgent completes the full fuzzing lifecycle for all 20 libraries without human intervention and reaches 179619 branches, exceeding OSS-Fuzz, PromptFuzz, PromeFuzz, and OSS-Fuzz-Gen by 45.1%, 73.2%, 92.1%, and 191.2%, respectively. FuzzAgent also identifies 102 genuine library bugs, 78 of which have already been acknowledged and fixed by upstream maintainers.
