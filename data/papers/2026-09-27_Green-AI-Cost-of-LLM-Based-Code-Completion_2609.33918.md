# Green AI: Cost of LLM-Based Code Completion

- arXiv ID: `2609.33918v1`
- Authors: Negar Alizadeh, Nishant Saurabh, Fernando Castor
- Published: 2026-09-27
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.33918v1) | [pdf](https://arxiv.org/pdf/2609.33918v1)

## Abstract

Code completion is one of the most widely used applications of large language models (LLMs) in software development. Open-weight LLMs are increasingly adopted for locally deployed code completion systems, partly due to privacy concerns. Despite advances in LLM accuracy, the energy cost of inference remains underexplored, particularly under large-context workloads and across programming languages. This study investigates the trade-off between accuracy and energy consumption in LLM-based code completion and how workload characteristics, context size, and model scale influence inference energy usage. We evaluate 25 open-weight LLMs on two workloads: repository-level next-line completion with varying context sizes on RepoBench, and fill-in-the-middle (FIM) code completion across Python, Java, and Rust on McEval. We analyze the influence of input tokens, output tokens, model size, and their interactions on energy consumption using correlation analysis and cluster-robust linear regression. Our findings show that the dominant drivers of energy consumption depend strongly on task structure. In RepoBench, energy consumption is primarily influenced by input context size and its interaction with model scale, whereas in McEval, output generation and its interaction with active parameter count dominate. Output generation is more energy-intensive per token than prompt processing. Across both benchmarks, smaller and heavily quantized models frequently achieve Pareto-optimal trade-offs, often providing accuracy comparable to larger FP16 models while consuming substantially less energy. Increasing model size or context length does not necessarily lead to proportionally better completion quality, while quantization can substantially improve energy efficiency with limited accuracy degradation. These findings support more energy-aware deployment strategies for sustainable AI-assisted software development.
