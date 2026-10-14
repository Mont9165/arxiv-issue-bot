# Thinking More, Harnessing Better: State Machine Guided Harness Automatic Generation with Project Digestion and Workflow Decomposition

- arXiv ID: `2607.07007v1`
- Authors: Xing Zhang, Zikang Huang, Gang Yang, CongChong Wang, Lu Liu, Bin Yin, Mingyi Wang, Ziquan Zhao, Min Li, Zhenyu Chen, Bo Wu, Lingyun Ying
- Published: 2026-07-08
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.07007v1) | [pdf](https://arxiv.org/pdf/2607.07007v1)

## Abstract

High-quality fuzz harnesses are essential for effective gray-box fuzzing. While Large Language Models (LLMs) offer promise for automating this task, existing one-turn generation methods suffer from hallucinations and inadequate coverage due to coarse-grained function targeting and misaligned generation workflows. We present SynapseFlow, an automatic harness generator that addresses these limitations through two key innovations: dataflow-aware function aggregation and a staged, rollback-enabled generation workflow decomposition. SynapseFlow first analyzes source code to construct Structural Flow Graphs and extract coherent Function Triplets. It then synthesizes harnesses via a decomposed four-stage process governed by a staged rollback algorithm to ensure correctness. We evaluated SynapseFlow on 25 real-world open-source software projects. The experimental results indicate that SynapseFlow outperforms state-of-the-art tools (OSS-Fuzz-Gen, CKGFuzzer, PromeFuzz), achieving 3.07$\times$, 1.71$\times$, and 4.26$\times$ higher branch coverage, and 1.77$\times$, 1.51$\times$, and 1.36$\times$ higher bug detection rates, respectively. Most importantly, SynapseFlow discovered 7 previously unreported bugs (5 assigned CVEs), demonstrating its practical effectiveness in real-world bug discovery.
