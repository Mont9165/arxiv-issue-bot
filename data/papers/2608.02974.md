# ConFL: Explainable Concurrent Fault Localization via Hierarchy-Guided LLM Reasoning

- arXiv ID: `2608.02974v1`
- Authors: Shuai Shao, Dingbang Wang, Yiming Zeng, Tingting Yu
- Published: 2026-08-04
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.02974v1) | [pdf](https://arxiv.org/pdf/2608.02974v1)

## Abstract

Localizing concurrent bugs from bug reports alone is challenging due to incomplete information, misleading program-entity mentions, and complex cross-thread interactions, causing existing LLM-based approaches to suffer from unstable reasoning and limited explainability. We propose ConFL, an explainable concurrent fault localization framework that augments LLM reasoning with structured concurrency knowledge. ConFL constructs a Concurrent Knowledge Base (CKB) from source code and performs LLM-guided hierarchical retrieval to progressively narrow the search space from components to interaction-level concurrency contexts. An interaction-level DSL explicitly encodes cross-thread interactions over shared resources, enabling focused reasoning without traversing deep call chains. Experiments on real-world concurrent bugs from eight large-scale Java projects show that ConFL significantly outperforms state-of-the-art IR-based and LLM-based baselines, achieving an MRR of 0.503 and a MAP of 0.486, while remaining robust to noisy bug reports, unseen bugs, and different LLM backbones.
