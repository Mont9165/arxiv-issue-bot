# Green Code or Costly Code? Evaluating the Energy Costs of Iterative LLM-Based Code Optimizations

- arXiv ID: `2610.32891v1`
- Authors: Sadra Emami, Benjamin Weigell, Mohammad Reza Mousavi, Gunel Jahangirova, Hugo Araujo, Bernhard Bauer
- Published: 2026-10-23
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2610.32891v1) | [pdf](https://arxiv.org/pdf/2610.32891v1)

## Abstract

Large Language Models (LLMs) are increasingly used to optimize code for performance. This practice often assumes that improvements in execution speed naturally translate into overall lower energy consumption. We challenge this assumption empirically by measuring whether performance-optimized code produced by LLM self-refinement pipelines is also energy-efficient relative to canonical human reference solutions, and whether the energy cost of the optimization process can be offset by subsequent execution-time savings. We evaluate 11 open-source models across four decoding configurations on all 1,000 problems of EffiBench, a state-of-the-art performance benchmark, while collecting per-process, hardware-level energy measurements throughout. Inference energy spans 0.79 to 8.68 MJ across model-variant pairs, which is roughly equivalent to the energy of 250 to 2800 GPT-4.1 queries. Limiting the maximum number of output tokens has the largest impact, reducing energy use by up to 69% compared to the default configuration. On the execution side, 42 of 44 configurations produce code that consumes more energy per problem than the canonical human reference, with overheads ranging from +4% to +886%. The two exceptions achieve only marginal gains, with break-even points on the order of 10^6 to 10^7 executions. Mixture-of-Experts architectures consume substantially less inference energy than equivalently-sized dense models without sacrificing correctness, making architectural choice a more consequential sustainability lever than decoding parameters. Performance optimization and energy efficiency are not always aligned goals: LLM self-refinement consistently produces faster-seeking but energy-heavier code relative to what a human engineer would write. All artifacts are available at https://doi.org/10.5281/zenodo.23598170.
