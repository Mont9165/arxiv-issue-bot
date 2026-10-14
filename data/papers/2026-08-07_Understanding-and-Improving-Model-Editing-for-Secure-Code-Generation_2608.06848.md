# Understanding and Improving Model Editing for Secure Code Generation

- arXiv ID: `2608.06848v1`
- Authors: Weifeng Sun, Quanjun Zhang, Yuchen Chen, Chengran Yang, Gou Tan, David Lo
- Published: 2026-08-07
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.06848v1) | [pdf](https://arxiv.org/pdf/2608.06848v1)

## Abstract

Large language models (LLMs) are widely used for code generation, yet they can reproduce vulnerable implementations learned from insecure training patterns. Prior work has mainly explored inference-time hardening, which reduces insecure generations without modifying the target model but relies on auxiliary components and adds runtime overhead. We conduct the first systematic study of model editing as a model-level hardening mechanism for secure code generation. We evaluate 3 state-of-the-art editing methods across diverse LLM families and compare them with CoSec, a representative inference-time approach, focusing on security, robustness, generalization, and functional correctness. Model editing yields larger security gains than CoSec on seen vulnerability types, improving security ratios by 15%-25% over vanilla models, with gains remaining stable under prompt perturbations. However, these improvements transfer unreliably to unseen vulnerabilities and can reduce functional correctness. To mitigate this trade-off, we propose SafeEdit, a post-edit refinement method combining functional tuning with edit-aware regularization. Across eight target LLMs, SafeEdit improves Pass@1 over UltraEdit by 11.73/13.70/15.50 percentage points at T=0.1/0.4/0.8 while largely preserving security. Compared with CoSec, it achieves relative security-ratio gains of 7.54%-12.04%. Additional evaluation on CodeGuard+ confirms improved joint secure-and-correct generation. SafeEdit and CoSec are also complementary, and their combination can further improve security while maintaining strong functional correctness. Overall, our results provide evidence-backed guidance for applying model editing to secure code generation.
