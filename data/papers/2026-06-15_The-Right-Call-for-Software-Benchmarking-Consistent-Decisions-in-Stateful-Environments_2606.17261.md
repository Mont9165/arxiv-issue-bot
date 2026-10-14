# The Right Call for Software Benchmarking: Consistent Decisions in Stateful Environments

- arXiv ID: `2606.17261v1`
- Authors: Gábor Melis
- Published: 2026-06-15
- Primary category: `cs.PF`
- Categories: `cs.PF`, `cs.SE`, `stat.AP`
- Links: [abs](http://arxiv.org/abs/2606.17261v1) | [pdf](https://arxiv.org/pdf/2606.17261v1)

## Abstract

In the perpetual pursuit of performance, modern computing systems rely ever more on stateful mechanisms to accommodate the dynamics of workloads and physical environments, bolstering efficiency but confounding benchmarking and thereby the optimization of software. Indeed, by their nature, adaptive mechanisms introduce temporal dependencies between measurements and render naive estimators of individual program performance biased. Observing that rectifying such biases necessitates speculative assumptions about system dynamics, we call for prioritizing performance differentials over absolute measures and formalize software benchmarking as the decision problem of identifying the fastest program, for which relative knowledge suffices. To this end, we propose simple experiment designs admitting consistent estimators of contrasts, whereby program-specific biases cancel under tenable assumptions. These designs asymptotically yield the correct decision and afford a robust methodology for finite-budget benchmarking in stateful environments, bearing broad implications for the development of performance-sensitive software.
