# Two Truths and A Lie? Benchmarking Off-the-Shelf LLMs for Requirements Quality Assessment: Performance, False Alarms, and Misses

- arXiv ID: `2609.03230v1`
- Authors: Jannatul Shefa, Alejandro Salado, Paul Wach, Taylan G. Topcu
- Published: 2026-09-03
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.03230v1) | [pdf](https://arxiv.org/pdf/2609.03230v1)

## Abstract

Requirements engineering (RE) governs the quality of everything downstream in systems engineering (SE); defective requirements that survive review cycles propagate into design rework, schedule delays, and cost overruns. Because requirements are often written in natural language, recent advances in generative AI have raised expectations that large language models (LLMs) can absorb requirement quality assessment, a task otherwise slow and human expertise-intensive. Yet empirical evidence on whether LLMs can be trusted to do so remains scarce. This study presents the first benchmarking analysis of off-the-shelf LLM performance for requirement quality evaluation. Against an expert-derived ground truth built on INCOSE quality criteria, we evaluate ten models spanning two families (OpenAI and Anthropic) and five generations each, across one hundred independent runs, two requirement sets, and five sampling temperatures. Four contributions follow. First, we quantify a strongly asymmetric error profile: across all models and runs, the best-performing Anthropic model detects a median of only 47% of expert-identified issues while false-flagging 11%. Second, performance degrades significantly where SE judgment is required, as necessity and correctness issues are almost always missed. Third, generational progress is non-monotonic, so newer models cannot be assumed better. Fourth, this error behavior shifts only modestly and non-monotonically across sampling temperatures, indicating characteristic model deficiencies rather than inherent stochasticity. Off-the-shelf LLMs are therefore not yet trustworthy autonomous evaluators. Findings also warrant caution for Agentic AI developers: orchestrating these LLM modules in specialized architectures risks compounding these deficiencies rather than correcting them. Their defensible near-term role is human-in-the-loop decision support.
