# Planning to Hammer: Difficulty-Aware Decomposition for Automating Rocq Proofs

- arXiv ID: `2606.17981v1`
- Authors: Ning Zhang, Nongyu Di, Zenan Li, Yuan Yao, Xiaoxing Ma
- Published: 2026-06-16
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.17981v1) | [pdf](https://arxiv.org/pdf/2606.17981v1)

## Abstract

As AI-generated code proliferates, formal verification, particularly through interactive theorem provers such as Rocq and Isabelle, becomes increasingly important for ensuring software correctness. However, producing machine-checked proofs in such provers remains a bottleneck. Existing solutions bring complementary strengths to proof automation: large language models (LLMs) can propose high-level proof strategies but lack local rigor, while automated tactics such as CoqHammer can reliably discharge many local goals but lack long-range planning capabilities. To combine the best of both worlds, we present Quarry, a planning-based proof synthesis framework that separates proof planning from proof execution. Specifically, Quarry asks an LLM to actively propose multiple proof decompositions with arbitrary sublemmas, type-checks them in Rocq under temporarily admitted sublemmas, and ranks candidates using a proof-state-based difficulty model that estimates hammer solvability. It then recursively proves sublemmas within a bounded budget, effectively turning long proofs into sequences of hammer-solvable obligations. We implement Quarry on top of SerAPI and CoqHammer and evaluate it using multiple frontier LLMs across multiple benchmarks. The experimental results show that planning-based decomposition with solvability-aware ranking substantially improves automation while maintaining predictable cost. Under a uniform 10-minute wall-clock budget, Quarry improves over the strongest baseline by 7% to 13% in success rate across three Rocq benchmarks. These results demonstrate that reliable proof automation can be achieved by coordinating neural planning with symbolic execution rather than replacing either.
