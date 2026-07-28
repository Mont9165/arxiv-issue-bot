# ABISS: Evaluating Text-to-SQL Systems Through Agent Interaction

- arXiv ID: `2607.23340v1`
- Authors: Giovanni Sullutrone, Luca Sala, Sania Aftar, Georgia Koutrika, Sonia Bergamaschi
- Published: 2026-07-25
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.23340v1) | [pdf](https://arxiv.org/pdf/2607.23340v1)

## Abstract

Large Language Models (LLMs) demonstrate high performance on curated Text-to-SQL benchmarks; nevertheless, real-world users frequently pose ambiguous or unanswerable questions that current systems handle poorly. Three interconnected gaps hinder progress: incomplete taxonomies, realistic benchmark generation for real-world settings, and static user interaction. We address all of the above issues through three contributions: (1) a unified taxonomy of 8 categories covering ambiguous and unanswerable questions; (2) a multi-agent generation pipeline with a two-stage process (NLQ generation followed by SQL grounding) and an explicit Category Conformance validation stage, producing questions from arbitrary databases validated by a council of local open-source models; and (3) ABISS (Ambiguity Benchmark using Interaction-Simulated Sessions), a dynamic simulation environment where Text-to-SQL agents interact with style-aware simulated users across multi-turn dialogues. Experiments with eight open-source models on ABISS-BIRD and ABISS-Spider reveal two fundamental bottlenecks. The first is subcategory classification: models detect that a question is problematic yet struggle to pinpoint the specific subcategory. The second is clarification-conditioned SQL generation: even after receiving useful user information, models often still fail in the final resolution step. Providing the ground truth category yields large gains in both execution and feedback across both datasets, yet ambiguous-question execution remains low even under oracle category labels. We release our code for data generation and benchmark on GitHub (https://github.com/giosullutrone/ABISS-Evaluating-Text-to-SQL-Systems-Through-Agent-Interaction).
