# SpecAgent: Empowering Program Verification with Agentic Synthesis of Formal Program Specifications

- arXiv ID: `2610.05132v1`
- Authors: Lezhi Ma, Han Wang, Shangqing Liu, Jiawan Wang, Lei Bu
- Published: 2026-10-04
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.05132v1) | [pdf](https://arxiv.org/pdf/2610.05132v1)

## Abstract

Formal specifications are essential for deductive program verification, providing semantic abstractions for compositional verification of complex software. However, manually constructing specifications is labor-intensive, motivating automated synthesis. Despite recent advances in large language models (LLMs), existing approaches often rely on forward-only workflows and localized repair, limiting their effectiveness on real-world programs with complex dependencies among functions and loops. Verification failures may stem from previously generated specifications, causing cascading failures that local refinement cannot resolve. To address these challenges, we present SpecAgent, an agentic framework for synthesizing high-quality ACSL specifications for real-world C programs. SpecAgent integrates four components: dependency-aware planning to identify specification targets, retrieval-augmented generation (RAG) to provide relevant specification patterns and program context, agentic repair to diagnose defects and revisit dependent specifications, and agentic critique to assess and refine semantic strength beyond proof success. We evaluate SpecAgent on specification synthesis and program verification tasks. On 50 programs from 14 real-world repositories, SpecAgent with DeepSeek-V4 achieves 96.82% precision and 88.95% recall in synthesizing correct and strong specifications, outperforming all baselines. On 811 real-world verification targets, it successfully discharges 604, also surpassing existing baselines. These results demonstrate SpecAgent's effectiveness in synthesizing high-quality specifications and facilitating real-world program verification.
