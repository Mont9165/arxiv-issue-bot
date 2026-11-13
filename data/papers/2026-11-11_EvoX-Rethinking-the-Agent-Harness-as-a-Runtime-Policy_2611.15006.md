# EvoX: Rethinking the Agent Harness as a Runtime Policy

- arXiv ID: `2611.15006v1`
- Authors: Haoyang Zhang, Qumeng Sun, Xiao Zhang, Xiang Liu, Zhidong Fan, Junjie Wang
- Published: 2026-11-11
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.15006v1) | [pdf](https://arxiv.org/pdf/2611.15006v1)

## Abstract

Large language model (LLM) agents increasingly interact with tools and environments, yet plausible model decisions do not always translate into successful execution due to tool-call mismatches, interrupted workflows, and unsupported completion claims. We present EvoX, a Rust-based, multi-model agent runtime guided by The Second Policy, which views the harness as an Operational Policy complementing the foundation model's Semantic Policy. EvoX combines model-facing guidance with deterministic runtime control through three complementary mechanisms: Action Realization, Execution Continuity, and Outcome Grounding. To evaluate harnesses without suppressing their native behaviors, we introduce Contrast, a controlled and auditable framework integrating explicit fairness constraints, provider-bound request verification, and evidence-based adjudication. Across five benchmarks, six foundation models, and six agent harnesses, EvoX achieves the highest numerical success rate of 56.2% over 691 common task--model pairs, exceeding the average of the other five harnesses by approximately 3.0 percentage points. Its larger advantages on GLM-5.3 (+10.7 points) and Kimi K3 (+7.9 points) highlight the model-dependent effectiveness of harness design and the potential for cross-provider adaptability. Achieved without memory, evolution, or extensions, these results establish EvoX as a competitive multi-model agent runtime and underscore the importance of harness-level operational control in realizing foundation-model capabilities.
