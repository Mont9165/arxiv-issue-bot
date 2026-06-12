# Characterizing Software Aging in GPU-Based LLM Serving Systems

- arXiv ID: `2606.11916v1`
- Authors: Domenico Cotroneo, Bojan Cukic
- Published: 2026-06-10
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.11916v1) | [pdf](https://arxiv.org/pdf/2606.11916v1)

## Abstract

This paper proposes an empirical methodology to study software aging in GPU-based LLM serving systems. Traditional aging studies focus on CPU-centric software with relatively regular workloads; LLM serving is different, spanning a Python host and a CUDA device, handling requests whose cost varies by orders of magnitude, and relying on rapidly evolving software stacks. We run a 216-hour campaign across six co-located deployments under identical stress conditions, monitor host, device, and client metrics in parallel, and apply a statistical pipeline that accounts for autocorrelation and multiple testing. Our results reveal statistically significant memory aging in all deployments, with leak rates strongly dependent on the serving runtime and deployment configuration. Beyond these findings, we provide a reproducible framework that opens a research direction at the intersection of the software aging and rejuvenation and LLM serving communities.
