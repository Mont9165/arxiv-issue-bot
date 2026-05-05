# AI-Generated Smells: An Analysis of Code and Architecture in LLM and Agent-Driven Development

- arXiv ID: `2605.02741v1`
- Authors: Yuecai Zhu, Nikolaos Tsantalis, Peter C. Rigby
- Published: 2026-05-04
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.02741v1) | [pdf](https://arxiv.org/pdf/2605.02741v1)

## Abstract

The promise of Large Language Models in automated software engineering is often measured by functional correctness, overlooking the critical issue of long term maintainability. This paper presents a systematic audit of technical debt in AI-generated software, revealing that AI does not eliminate flaws but rather introduces a distinct machine signature of defects. Our multi-scale analysis, spanning single-file algorithmic tasks and complex, agent generated systems, identifies a fundamental Reasoning-Complexity Trade-off: as models become more capable, they generate increasingly bloated and coupled code. This architectural decay is so pronounced that we establish a Volume-Quality Inverse Law, where code volume is a near perfect predictor of structural degradation. Crucially, we demonstrate that neither functional correctness nor detailed prompting mitigates this decay. These findings challenge the current paradigm of prompt-driven generation, reframing the central problem of AI-based software engineering from one of code generation to one of architectural complexity management. We conclude that future progress depends on equipping agents with explicit architectural foresight to ensure the software they build is not just functional, but also maintainable.
