# Attention to Detail: Evaluating Energy, Performance, and Accuracy Trade-offs Across vLLM Configurations

- arXiv ID: `2607.09172v1`
- Authors: Nada Zine, Tristan Coignion, Vincenzo Stoico, Clément Quinton, Romain Rouvoy, Patricia Lago
- Published: 2026-07-10
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.PF`
- Links: [abs](http://arxiv.org/abs/2607.09172v1) | [pdf](https://arxiv.org/pdf/2607.09172v1)

## Abstract

Large Language Models are reshaping how software is developed and maintained. They are typically deployed in production using inference engines such as vLLM, which can efficiently serve pre-trained, highly configurable models. While prior work has focused on model architectures and hardware acceleration, the impact of inference engine configuration on energy consumption, performance, and output quality remains poorly understood.
  In this paper, we present a large-scale controlled study of three selected vLLM configuration options: attention kernel type, prefix caching, and chunked prefill. We evaluate all combinations of these configurations across 5 open-weight LLMs and 5 diverse inference tasks, totaling $9,000$ runs and $93,600$ measures. We analyze energy consumption, latency, and accuracy, and examine both main effects and interaction effects between configuration options and tasks.
  Our results show that the studied configuration options significantly impact energy and performance, mainly driven by attention type and prefix caching, while chunked prefill has a limited effect under the default vLLM serving configuration and evaluated workloads. These effects are highly model- and workload-dependent, and no configuration is universally optimal. We further show that model choice dominates global trade-offs, while configuration tuning provides local improvements along the Pareto frontier. Unexpectedly, inference options can also affect model accuracy.
