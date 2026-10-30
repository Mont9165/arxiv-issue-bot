# Lost in the Latent Space: How Code Embeddings Represent Functional Intent and Implementation Fidelity

- arXiv ID: `2610.39519v1`
- Authors: Lu Sun, Yuheng Huang, Lei Ma, Zhijie Wang
- Published: 2026-10-29
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2610.39519v1) | [pdf](https://arxiv.org/pdf/2610.39519v1)

## Abstract

Code embedding models have become a key building block for many software engineering applications, yet their internal representations remain poorly understood. Existing evaluations tend to focus on downstream task performance, offering limited insight into whether a single embedding can support both functional abstraction and implementation-sensitive analysis. To address this gap, we present a large-scale empirical study of 14 state-of-the-art code embedding models. We evaluate their representational behavior through three complementary analyses: supervised probing for functional abstraction and implementation fidelity, zero-shot retrieval experiments to assess geometric similarity, and controlled perturbation experiments that measure embedding responses to semantics-preserving code transformations. The results reveal a consistent abstraction-fidelity tension: models that better preserve stylistic and structural signals tend to do so at the expense of semantic generalization, while models with similar retrieval performance can nevertheless respond very differently to the same implementation changes. Overall, our findings suggest that a single universal code representation remains out of reach, motivating more representation-aware evaluation, selection, and deployment of code embedding models in software engineering.
