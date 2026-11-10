# RealEmbedBench: Benchmarking LLMs on Real-World Application-Layer Embedded Software Tasks

- arXiv ID: `2611.11469v1`
- Authors: Yujun Huang, Yuwei Zhang, Yi Zhou, Shanshan Wu, Xiang Chen, Lina Gong
- Published: 2026-11-08
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.11469v1) | [pdf](https://arxiv.org/pdf/2611.11469v1)

## Abstract

Large language models (LLMs) perform well on general coding tasks, but their capabilities in application-layer embedded software development remain underexplored. Existing embedded benchmarks primarily focus on hardware-in-the-loop validation in simulated environments. We introduce RealEmbedBench, a benchmark of 5,142 samples covering three application-layer tasks: code generation and completion, state machine modeling and implementation, and cross-OS code translation. We evaluate six representative LLMs and find substantial performance differences across tasks and models. Project context, especially the local code window, significantly affects code generation and completion. Models perform reasonably well at state machine modeling but struggle to translate these models into executable code. Cross-OS translation performance varies substantially by direction. Translation from Harmony to RT-Thread is particularly challenging, with an average pass rate of 0.1667. These findings suggest that developers should consider local code context when using LLMs for code generation and completion and select models according to the translation direction. They also motivate the use of more real-world state machine implementation data in LLM training to narrow the gap between modeling and executable code.
