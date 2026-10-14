# EviACT: An Evidence-to-Action Framework for Agentic Program Repair

- arXiv ID: `2605.27238v1`
- Authors: Qianru Meng, Xiao Zhang, Zhaochun Ren, Joost Visser
- Published: 2026-05-26
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.27238v1) | [pdf](https://arxiv.org/pdf/2605.27238v1)

## Abstract

LLM-based agents have moved automated program repair (APR) from fixed-context patch generation to interactive repository-level repair. However, existing agentic APR systems still struggle to use execution evidence to guide localization, patch generation, and validation. We propose EviACT (Evidence-to-Action), an agentic APR framework that coordinates three evidence-driven guardrails across repair stages. The retrieval scaffold grounds repair context, the compile gate filters invalid edits, and the test-driven gate checks target-test recovery before full regression. Across four benchmarks, EviACT improves resolve rate over the strongest reported comparable baselines by 1.6-6.0 percentage points and shows 70.1-88.6% lower reported per-bug API cost where baseline costs are available. Ablations and diagnostics suggest that these gains are associated with the coordinated evidence-to-action chain, making agentic APR more effective and efficient.
