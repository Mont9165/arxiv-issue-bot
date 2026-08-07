# KVerus: Scalable and Resilient Formal Verification Proof Generation for Rust Code

- arXiv ID: `2605.03822v1`
- Authors: Yuwei Liu, Xinyi Wan, Yanhao Wang, Minghua Wang, Lin Huang, Tao Wei
- Published: 2026-05-05
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2605.03822v1) | [pdf](https://arxiv.org/pdf/2605.03822v1)

## Abstract

Formal verification provides the highest assurance of software correctness and security, but its application to large-scale, evolving systems remains a major challenge. While large language models (LLMs) have shown promise in automating proof generation, they often fail in real-world settings due to their inability to handle complex cross-module dependencies or changes in the codebase or the verification toolchain. We identify the fundamental problem as the Semantic-Structural Gap: LLMs operate on semantic code patterns, whereas formal verification is governed by rigid structural dependencies, a disconnect that leads to brittle, unsustainable proofs.
  To bridge this gap, we propose a new paradigm of self-adaptive verification and present KVerus, a retrieval-augmented system for Verus-based Rust verification that can adapt to an evolving software environment. KVerus constructs a dynamic knowledge base of code metadata, lemma semantics, and toolchain specifics. By combining dependency-aware program analysis, semantic lemma indexing, and error-driven self-refinement, it can navigate intricate cross-file dependencies to synthesize proofs and automatically repair proofs when faced with common evolutionary changes. Across three single-file benchmarks, KVerus verifies 80.2% of tasks, outperforming the state-of-the-art AutoVerus (56.9%) and degrades less than AutoVerus under breaking Verus updates. On three repository-level benchmarks with cross-file dependencies, KVerus achieves a 51.0% success rate, compared to 4.5% for a multi-round prompting baseline. Finally, on the Asterinas Rust OS kernel, KVerus produces upstream-accepted proofs that verify 23 previously unverified functions (21.0% of proof code) in the memory-management module. KVerus represents a significant step towards making formal verification a scalable and sustainable practice for modern, security-critical software.
