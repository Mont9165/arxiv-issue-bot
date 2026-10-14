# LLMs in Digital EDA: A perspective on shifting roles from Generation to Orchestration

- arXiv ID: `2608.27184v1`
- Authors: Matthew Youngman, Cristian Sestito, Themis Prodromakis
- Published: 2026-08-27
- Primary category: `cs.AR`
- Categories: `cs.AR`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.27184v1) | [pdf](https://arxiv.org/pdf/2608.27184v1)

## Abstract

Electronic design automation (EDA) has advanced engineering productivity through successive generations of tooling that progressively automate synthesis, optimisation, and verification. Large language models (LLMs) extend this trajectory by enabling direct translation from design intent to hardware implementations. In most of the EDA literature, LLM-based solutions are typically assisting siloed design stages or tasks, however this obscured the drivers by which capability emerges and systems scale. In this Perspective, we instead define three hierarchical roles that reveal how capability accumulates: a Generator that produces design artifacts in a single pass, an Agent that refines outputs through iterative tool feedback, and an Orchestrator that coordinates decisions across EDA-stages. Across published systems, this reveals a syntax trap in which models are trained to produce plausible code rather than physically correct hardware, compounded by fragmented tools and loss of design context that obscure how decisions affect later stages. Comparisons across the three roles show that current approaches struggle to scale to industrial designs, motivating a shift towards a standardised, physics-aware orchestrator that connects tools and agents across the EDA flow for more reliable and accessible hardware design.
