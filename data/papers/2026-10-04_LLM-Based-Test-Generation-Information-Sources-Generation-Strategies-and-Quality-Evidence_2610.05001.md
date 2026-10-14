# LLM-Based Test Generation: Information Sources, Generation Strategies, and Quality Evidence

- arXiv ID: `2610.05001v1`
- Authors: Yunhao Liang, Chengguang Gan, Ruixuan Ying, Hanjun Wei, Zhe Cui, Shiwen Ni
- Published: 2026-10-04
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.05001v1) | [pdf](https://arxiv.org/pdf/2610.05001v1)

## Abstract

Large language models are increasingly used to generate test scenarios, executable test suites, assertions, interaction sequences, and fuzzing infrastructure. These artifacts serve different purposes and rely on different sources of information about correct behavior. A test that increases implementation coverage, a test that agrees with a reference program, and a test that detects a requirements violation therefore provide distinct kinds of evidence. We present a structured narrative survey that connects the generation process to the evidence used to justify test quality. Drawing on 95 curated source records through 29 September 2026, we organize the field along four dimensions: testing objectives and artifacts, information available during training and generation, generation and learning mechanisms, and evaluation evidence. We synthesize work on unit and requirements-based testing, test oracles, API and GUI testing, fuzzing, and learned test generators. The resulting framework explains how execution feedback can improve executability while also affecting the independence of an oracle, why specification provenance and training-time reference supervision matter for comparisons, and how downstream code-selection gains differ from test correctness. We use these distinctions to organize benchmarks and derive a research agenda for independent oracle assessment, budget-aware generation, repository-scale evaluation, and test maintenance.
