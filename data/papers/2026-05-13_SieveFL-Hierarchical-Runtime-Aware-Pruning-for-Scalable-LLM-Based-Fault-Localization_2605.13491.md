# SieveFL: Hierarchical Runtime-Aware Pruning for Scalable LLM-Based Fault Localization

- arXiv ID: `2605.13491v1`
- Authors: Mahdi Farzandway, Fatemeh Ghassemi
- Published: 2026-05-13
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.13491v1) | [pdf](https://arxiv.org/pdf/2605.13491v1)

## Abstract

Automated fault localization requires connecting an observed test failure to the responsible method across thousands of candidates--a task that purely statistical approaches handle with limited precision and that LLMs cannot yet handle at full project scale due to prohibitive token cost and signal dilution. We present SieveFL, a five-stage hierarchical framework that resolves this tension through aggressive pre-LLM filtering. SieveFL converts a failing test into a natural-language failure description, uses dense vector retrieval to narrow the search to a small set of suspicious files, and then eliminates any method not executed during the failing test via JaCoCo runtime traces. Only the surviving candidates are passed to the LLM, which screens each method individually and re-ranks the confirmed suspects in a single comparative pass. We evaluate SieveFL on 395 bugs from Defects4J v1.2.0 using a mid-sized, openly available MoE model deployed on a commodity workstation (32 GB RAM, 8 GB GPU) via Ollama--no frontier APIs or datacenter hardware required. Treating 12 incomplete runs as failures, SieveFL achieves Top-1 accuracy of 41.8% (165/395 bugs) and an MRR of 0.469, outperforming the strongest prior agent-based baseline (AgentFL) by 2.1 pp in Top-1. Runtime pruning removes 79% of candidate methods and reduces input token consumption by 49%, while simultaneously improving ranking quality: Top-1 is preserved exactly and Top-3 through Top-10 improve by up to 2.4 pp. These results demonstrate that, with the right filtering architecture, capable fault localization does not require proprietary frontier models.
