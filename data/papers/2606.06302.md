# Tangram: Unlocking Non-Uniform KV Cache for Efficient Multi-turn LLM Serving

- arXiv ID: `2606.06302v1`
- Authors: Hyungmin Kim, Minsoo Kim, Hongseok Kim, Jungwook Choi
- Published: 2026-06-04
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.06302v1) | [pdf](https://arxiv.org/pdf/2606.06302v1)

## Abstract

Multi-turn Large Language Model (LLM) serving is critical for consistent user experiences, yet the linear growth of the Key-Value (KV) cache imposes significant pressure on GPU memory and bandwidth. Non-uniform KV compression effectively preserves more information by considering the individual importance of each KV cache. However, such KV cache heterogeneity introduces various systemic challenges - including memory fragmentation, scheduling complexities, and diminished kernel utilization - which collectively lead to significant inefficiencies in existing LLM serving systems.
  To overcome these challenges, we present Tangram, a novel serving system designed to make Non-uniform KV caches practical. Tangram addresses systemic inefficiencies through three core techniques: (1) Deterministic Budget Allocation assigns a static memory footprint to each head based on its intrinsic pattern, entirely eliminating dynamic scheduling overhead and prefill stalls; (2) Head Group Page clusters attention heads with similar retention demands and manages them with independent, vectorized page tables, thereby maximizing physical memory reclamation; and (3) Ahead-of-Time (AOT) Load Balancing leverages static budget profiles to ensure uniform GPU utilization without runtime overhead. Experimental results show that Tangram improves throughput by up to 2.6x compared to existing baselines, while fully preserving model accuracy. Our implementation is publicly available at https://github.com/aiha-lab/TANGRAM.
