# Designing an Auditable LLM-Supported Workflow for Qualitative Thematic Analysis

- arXiv ID: `2608.30543v1`
- Authors: Nadia Jul Jeldtoft, Tariq Yousef
- Published: 2026-08-31
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.30543v1) | [pdf](https://arxiv.org/pdf/2608.30543v1)

## Abstract

Large Language Models (LLMs) offer new possibilities for scaling qualitative analysis, but existing applications often provide limited methodological transparency regarding how qualitative methods are translated into computational procedures. This paper presents an auditable and privacy-preserving computational operationalization of inductive and latent Thematic Analysis (TA). This paper first derives five design principles from the methodological requirements of TA and the conditions introduced by LLM-based inference: preserving interpretative context, maintaining traceable relationships between empirical material and analytical outputs, representing analytical constructs and reasoning explicitly, constraining LLM inference to interpretative tasks, and enabling privacy-preserving local deployment. Second, it presents a proof-of-concept for a two-phase workflow that operationalizes these principles by combining interpretative LLM inference with deterministic procedural control to generate codes, analytical justifications, themes, and theme descriptions while preserving explicit links to the source material. Third, it proposes an evaluation framework combining structural comparison with human-led TA and independent expert assessment of analytical quality. The evaluation is conducted on semi-structured Danish interview transcripts. and the results shows that the workflow produces code-level outputs with coverage broadly comparable to human annotations and highly rated analytical justifications, while generating a more compressed thematic structure characterized by fewer and broader themes. The findings demonstrate the feasibility of auditable LLM-supported TA through a modular workflow designed to scale to larger datasets, accommodate different LLMs, and support transfer across research domains, with domain adaptation primarily requiring adjustments to the prompting strategy.
