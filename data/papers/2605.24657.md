# Beyond Inference-Only Deployment: Comparing Weight-Based Consolidation Against Cascading Compaction

- arXiv ID: `2605.24657v1`
- Authors: Simon Dennis, Kevin Shabahang, Hao Guo, Rivaan Patil
- Published: 2026-05-23
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.24657v1) | [pdf](https://arxiv.org/pdf/2605.24657v1)

## Abstract

Major LLM platforms deploy models in an inference-only configuration: the model serves requests but never updates per-user weights. Users must repeatedly re-teach preferences, corrections, and project context, and context-based workarounds consume context-window space and degrade under cascading compaction. We evaluate an alternative: nightly consolidation of interaction knowledge into model weights via reflection, synthesis, and Low-Rank Adaptation (LoRA) fine-tuning on a single consumer GPU. Across ten realistic software development conversations (n = 10, 1,146 test questions across three memory types), three cycles of cascading compaction retain 36.8 +/- 3.0% of knowledge (between an 11.8% no-context floor and a 90.1% full-context ceiling), while consolidation retains 80.4 +/- 1.3% -- a 43.6 pp gain (paired t(9) = 14.8, p < 0.001) that more than doubles what compaction preserves, with the largest gains on procedural corrections (36.3% -> 74.6%) and episodic project facts (31.5% -> 78.2%). As a methodological aside, mean per-token validation cross-entropy is negatively correlated with LLM-judged accuracy (r = -0.51) while median per-token validation cross-entropy tracks accuracy almost exactly (r = +0.99): under evaluators that tolerate surface-form variation, the mean is misleading and a heavy-tail-robust statistic is the faithful signal. Persistent personalization requires moving beyond inference-only deployment toward architectures that consolidate knowledge into weights.
