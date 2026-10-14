# Binary Decompilation LLM with Feedback-Driven Multi-Turn Refinement

- arXiv ID: `2606.16162v1`
- Authors: Peipei Liu, Jian Sun, Mingzhe Xing, Yicheng Zeng, Zhaoteng Yan, Lixiao Zhang, Li Chen, Dan Li
- Published: 2026-06-15
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.16162v1) | [pdf](https://arxiv.org/pdf/2606.16162v1)

## Abstract

Binary decompilation is fundamental to security tasks such as vulnerability discovery, malware inspection, and executable-only program understanding. Recent LLM-based decompilation methods have shown promising results, but most still follow a single-turn generation paradigm: given assembly code or decompiler-produced pseudo-code, the model generates one output and stops. Consequently, the generated code may appear readable or even compile successfully, yet still deviate from the behavior of the original binary and mislead downstream analysis.
  This paper presents AutoDecompiler, a decompilation-specialized LLM trained with reinforcement learning for feedback-driven multi-turn binary decompilation. Instead of treating decompilation as one-shot code generation, AutoDecompiler formulates it as an iterative refinement process, where the model revises generated code based on compilation, execution, and input/output testing feedback. To enable this process, we design decompilation-specific rewards that capture code validity, recompilability, execution consistency, and semantic fidelity. We further construct stage-aware diagnostic feedback from compiler errors, execution failures, and failed test cases, and introduce progress-aware trajectory rewarding and turn-aware advantage reweighting to encourage beneficial revisions while suppressing regressions.
  We train the AutoDecompiler family and evaluate it across different input settings, model scales, and benchmarks. Experimental results show that AutoDecompiler consistently outperforms its single-turn counterparts under the same model size and input setting, achieving clear improvements in behavioral re-executability. These results demonstrate that learning to exploit program feedback with reinforcement learning is an effective direction for improving the functional correctness of LLM-based binary decompilation.
