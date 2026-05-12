# GraphInstruct: A Progressive Benchmark for Diagnosing Capability Gaps in LLM Graph Generation

- arXiv ID: `2605.09997v1`
- Authors: Zihe Wei, Sheng Xiang, Ying Zhang, Changjun Jiang
- Published: 2026-05-11
- Primary category: `cs.SI`
- Categories: `cs.SI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.09997v1) | [pdf](https://arxiv.org/pdf/2605.09997v1)

## Abstract

Graph-structured data underpins applications from citation analysis and social-network modeling to molecular design and knowledge-graph construction, and Large Language Models (LLMs) are increasingly used as prompt-driven graph synthesizers. Classical graph-generation reviews catalog deep generative models and their evaluation primitives, but predate the LLM era and provide no foundation for evaluating instruction-following graph synthesis. Recent LLM-era benchmarks evaluate models along graph-type or task-domain axes; such organizations, however, average over structural complexity and cannot localize where in the complexity spectrum an LLM breaks down. To close this diagnostic gap, we introduce GraphInstruct, a progressive-complexity benchmark that stratifies LLM graph generation into six complexity levels and five evaluation dimensions, paired with 800 hand-authored instructions, 1,582 algorithmically synthesized reference solutions, and a 12-LLM capability evaluation across 45 (model, strategy) configurations. We find that discriminative power peaks at multi-constraint composition rather than reasoning depth, that no single prompting strategy dominates across levels or model families, and that domain-semantic constraints remain iteration-invariant under all tested methods -- pointing to retrieval rather than additional compute as the next research frontier. Atop the benchmark, a verification-guided iterative framework with constraint-aware adaptive prompting consistently surpasses the prompt-engineering ceiling on tested target models, demonstrating that the benchmark's fine-grained signals drive method development.
