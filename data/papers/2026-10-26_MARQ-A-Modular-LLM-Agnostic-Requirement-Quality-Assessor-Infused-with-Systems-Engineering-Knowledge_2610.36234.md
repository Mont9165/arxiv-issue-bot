# MARQ: A Modular, LLM-Agnostic Requirement Quality Assessor Infused with Systems Engineering Knowledge

- arXiv ID: `2610.36234v1`
- Authors: Jannatul Shefa, Alejandro Salado, Paul Wach, Taylan G. Topcu
- Published: 2026-10-26
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.36234v1) | [pdf](https://arxiv.org/pdf/2610.36234v1)

## Abstract

Requirements engineering (RE) is foundational to systems engineering (SE), as requirement defects can propagate downstream and adversely affect development outcomes. Although large language models (LLMs) are promising for requirement quality assessment, prior work shows that off-the-shelf models miss a large share of expert-identified defects, perform unevenly across quality criteria, and vary across executions. This study investigates whether infusing expert-derived SE knowledge can improve LLM-based requirement quality evaluation beyond off-the-shelf capability. We present MARQ, a modular, LLM-agnostic prototype that supplements LLMs with a criterion-specific knowledge stack operationalizing INCOSE requirement quality criteria and evaluated against off-the-shelf baselines on an expert-labeled NASA requirement set using Claude Opus 5, GPT-5.6 Sol, and the open-weight Gemma 3 12B, with 100 executions per model. MARQ achieves median F1 scores of 0.80 for Claude Opus 5, 0.62 for GPT-5.6 Sol, and 0.53 for Gemma 3 12B, compared with off-the-shelf baselines of 0.55, 0.52, and 0.18, respectively. However, the nature of these gains is model-dependent. Claude Opus 5 improves defect detection and false-alarm control; GPT-5.6 Sol gains detection and better execution-level consistency at the cost of more false alarms; and Gemma 3 12B reaches the performance of off-the-shelf proprietary models, although it remains highly variable. Criterion-level analysis shows gains concentrated in Correctness and Conformance, trade-offs between misses and false alarms within individual criteria, and model-dependent responses across several criteria. These findings position SE knowledge infusion as a promising model-agnostic pathway for strengthening trustworthy LLM-based RE support while underscoring the need for criterion-specific interventions and human-in-the-loop review.
