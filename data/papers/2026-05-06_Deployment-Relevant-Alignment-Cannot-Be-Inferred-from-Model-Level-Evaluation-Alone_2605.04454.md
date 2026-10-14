# Deployment-Relevant Alignment Cannot Be Inferred from Model-Level Evaluation Alone

- arXiv ID: `2605.04454v1`
- Authors: Varad Vishwarupe, Nigel Shadbolt, Marina Jirotka, Ivan Flechais
- Published: 2026-05-06
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.HC`, `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.04454v1) | [pdf](https://arxiv.org/pdf/2605.04454v1)

## Abstract

Alignment evaluation in machine learning has largely become evaluation of models. Influential benchmarks score model outputs under fixed inputs, such as truthfulness, instruction following, or pairwise preference, and these scores are often used to support claims about deployed alignment. This paper argues that deployment-relevant alignment cannot be inferred from model-level evaluation alone. Alignment claims should instead be indexed to the level at which evidence is collected: model-level, response-level, interaction-level, or deployment-level. Two studies support this position. First, a structured audit of eleven alignment benchmarks, extended to a sixteen-benchmark corpus, dual-coded against an eight-dimension rubric with Cohen's kappa = 0.87, finds that user-facing verification support is absent across every benchmark examined, while process steerability is nearly absent. The few interactional benchmarks identified, including tau-bench, CURATe, Rifts, and Common Ground, remain fragmented in coverage, and benchmark construction rather than data source determines what is measured. Second, a blinded cross-model stress test using 180 transcripts across three frontier models and four scaffolds finds that the same verification scaffold raises one model's verification support to ceiling while leaving another categorically unchanged. This shows that scaffold efficacy is model-dependent and that the gap identified by the audit cannot be closed at the model level alone. We propose a system-level evaluation agenda: alignment profiles instead of single scores, fixed-scaffolding protocols for comparable interactional evaluation, and reporting templates that make the inferential distance between evaluation evidence and deployment claims explicit.
