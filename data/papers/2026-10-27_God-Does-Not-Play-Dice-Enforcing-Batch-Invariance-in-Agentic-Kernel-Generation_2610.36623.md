# God Does Not Play Dice: Enforcing Batch Invariance in Agentic Kernel Generation

- arXiv ID: `2610.36623v1`
- Authors: Youwei Bao, Chengpeng Wang, Simin Chen
- Published: 2026-10-27
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.36623v1) | [pdf](https://arxiv.org/pdf/2610.36623v1)

## Abstract

Large language model (LLM) serving systems dynamically batch user requests for GPU execution, so the same request may be processed alongside different requests across runs. If the GPU kernels lack batch invariance (BI), this changing batch context can alter the numerical output for an unchanged input, undermining reproducibility. Existing kernel generation agents focus on correctness and efficiency but \emph{overlook BI}. We find 19 confirmed BI violations among 83 batch-applicable released artifacts. To address this limitation, we propose \tool, which combines contract-guided static dependency analysis with dynamic validation of bitwise consistency across batch contexts. \tool is designed as a plug-in component for general kernel agents, allowing their original optimization capabilities to be reused while adding BI enforcement. We integrate it as successive acceptance gates in the optimization loop, rejecting structurally risky or dynamically non-invariant candidates before performance benchmarking and returning feedback to the agent. Experiments across three agent frameworks under baseline and BI-aware generation on real world LLM serving tasks show that \tool improves the BI pass rate from 67.6\% to 91.9\% while retaining 91.8\% of the baseline geometric mean speedup. These results demonstrate that \tool can be incorporated into kernel optimization by agents as an additional reliability objective alongside correctness and speed.
