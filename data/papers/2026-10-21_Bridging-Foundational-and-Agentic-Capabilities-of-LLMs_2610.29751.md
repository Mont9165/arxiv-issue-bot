# Bridging Foundational and Agentic Capabilities of LLMs

- arXiv ID: `2610.29751v1`
- Authors: Wei Guo, Yuanjian Xu, Jianing Hao, Yongyao Duan, Ran Chen, Zhong Li, Guang Zhang
- Published: 2026-10-21
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.29751v1) | [pdf](https://arxiv.org/pdf/2610.29751v1)

## Abstract

Large language models (LLMs) are increasingly deployed as agents, yet it remains unclear how their foundational capabilities translate into agentic capabilities. End-to-end scores leave unresolved whether low benchmark capability or weak deployment drives a failure, limiting actionable diagnosis. We bridge foundational and agentic capabilities through an operation-level measurement framework. We represent each model with a foundational profile derived from capability benchmarks and an operation profile derived from interaction trajectories, and define capability realization gaps as deviations of observed operation performance from predictions based on foundational capabilities. Experiments on fifteen model services in $τ^2$-Bench show that foundational profiles only partially predict agentic operations. Models with comparable profiles can differ substantially in execution, and these gaps remain consistent across task subsets. Operation profiles add information and substantially improve task-score prediction. The framework locates execution departures at the operation level to inform model development and agent evaluation. We will release our code and analysis artifacts.
