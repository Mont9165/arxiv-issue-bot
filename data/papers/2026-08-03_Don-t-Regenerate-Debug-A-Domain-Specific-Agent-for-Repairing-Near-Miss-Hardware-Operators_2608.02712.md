# Don't Regenerate, Debug: A Domain-Specific Agent for Repairing Near-Miss Hardware Operators

- arXiv ID: `2608.02712v1`
- Authors: Yansong Sun, Shenxiu Wu, Siyuan Chen, Runlin Hou, Junhao Qiu, Junming Cao, Shudi Shao, Zhichao Lu, Qingfu Zhang
- Published: 2026-08-03
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2608.02712v1) | [pdf](https://arxiv.org/pdf/2608.02712v1)

## Abstract

Kernel generation for hardware accelerators such as GPUs and NPUs has become a proving ground for large language models (LLMs), and state-of-the-art systems raise correctness through pipelines that couple LLMs with agentic reinforcement learning and evolutionary search. Such pipelines generate, compile, and execute large numbers of candidate kernels, discarding most of them and forgoing the opportunity to distill failures into reusable knowledge. Many discarded candidates are near-miss operators that compile and run but fail numerical validation; each embodies genuine domain knowledge and a nontrivial investment in LLM inference, cross-compilation, and hardware execution. We argue for a paradigm shift: rather than regenerate, debug. Debugging is far more constrained than generating from scratch: the search space is small and feedback is dense. We present a domain-specific debug agent that addresses three core challenges in autonomous repair: mitigating knowledge scarcity through retrieved patterns and diagnostic instrumentation, ensuring integrity through anti-cheat detection and full-coverage evaluation, and controlling cost via convergence guards and bounded iteration. Debugging serves two complementary roles: it extends the capability frontier by recovering operators that repeated regeneration fails to produce, and it lowers cost per deliverable operator. Debug Pass@1 achieves 66.7% versus Regenerate Avg Pass@1's 25.9% and Regenerate Pass@3's 40.7%, while consuming 92.8% fewer tokens per success than three-trial regeneration. Component ablations show that the knowledge base drives recovery, while integrity gates reject 12.5-33.3% of the successes the workflow itself accepted.
