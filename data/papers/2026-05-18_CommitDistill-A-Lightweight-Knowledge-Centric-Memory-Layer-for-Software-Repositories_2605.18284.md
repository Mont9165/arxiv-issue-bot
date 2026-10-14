# CommitDistill: A Lightweight Knowledge-Centric Memory Layer for Software Repositories

- arXiv ID: `2605.18284v1`
- Authors: Divya Chukkapalli, Thejesh Avula, Aditya Aggarwal, Harsimran Singh, Amith Tallanki
- Published: 2026-05-18
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.18284v1) | [pdf](https://arxiv.org/pdf/2605.18284v1)

## Abstract

Software repositories accumulate large amounts of unstructured knowledge in commit messages, pull-request discussions, and issue threads, but developers and AI coding assistants rarely reuse this history effectively. Recent work on typed-memory architectures for LLM agents (MemGPT, generative agents, and the PlugMem module of Yang et al.) argues that agent memory should be distilled, typed knowledge rather than raw interaction text. We adapt that stance to a software repository's own git history under a constrained regime: deterministic, dependency-free, local-only, no embeddings. We present CommitDistill, an open-source Python prototype that mines a local git history into typed knowledge units (Facts, Skills, Patterns) using deterministic regex and surfaces them through a TF-IDF retriever with a calibrated silence threshold (theta = 2.5) that abstains on out-of-distribution queries. The artefact is a trust-instrumented memory substrate: deterministic, no external service, inspectable plain-JSON store, tunable abstention. A case study on five public repositories spanning Python, JavaScript, C, and Java (25,000 commits, 1,167 extracted units) reports useful-precision 0.525 at Cohen's kappa = 0.633 on 40 dual-annotated Python units. The decisive finding is budget-constrained retrieval: at a 256-character per-query budget, CommitDistill reaches 0.750 hit-rate on a 12-query benchmark against BM25's 0.333 and git log --grep's 0.083. On a four-arm paired LLM-as-judge evaluation (n=200 time-travel bug-fixes, two judges) covering control, CommitDistill, a body-budget-matched CD-Hybrid, and BM25, no condition produces a statistically detectable lift over control on the headline mean and CD-Hybrid is indistinguishable from BM25 head-to-head. Extraction over 10,000 commits completes in under 4 seconds on a laptop. Source, annotations, baselines, and a reproducibility script accompany this paper.
