# LYNX: Analytical Program Synthesis via Grounding and Closed-Loop Refinement

- arXiv ID: `2610.14777v1`
- Authors: Ruichen Xia, Xiao Han, Dingyu Yang, Luwei Yang, Sai Wu, Dongxiang Zhang, Binhui Yao, Gang Chen
- Published: 2026-10-10
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.14777v1) | [pdf](https://arxiv.org/pdf/2610.14777v1)

## Abstract

LLM-powered data analytics aims to translate natural language instructions into executable analytical programs over underlying data. However, existing approaches, whether treating LLMs as intent-to-code translators or as standalone analytical engines, often fail to reliably align domain semantics with complex schemas and heterogeneous metadata, resulting in brittle execution and semantically inconsistent analytical outputs in real-world workloads. We present LYNX, a multi-agent framework that formulates LLM-driven analytics as a schema- and knowledge-constrained analysis problem rather than a single-pass generation task. LYNX organizes analytical synthesis into a closed-loop workflow of planning, generation, verification, and refinement through three role-specialized agents that collaboratively enforce schema grounding, semantic consistency, and execution correctness. To address domain ambiguity and schema misalignment, LYNX integrates Semantic-Structural Distillation and Stage-Aware Allocation (SSD-SAA). A delta-guided iterative revision continuously diagnoses and repairs semantic and execution-level failures, substantially improving synthesis robustness. We evaluate LYNX on two NL-to-SQL benchmarks, BIRD-SQL Mini-Dev and the more challenging Spider 2.0-Lite. Experimental results demonstrate strong performance and efficiency, achieving 10.66% to 59.54% execution accuracy across lightweight and commercial models, while reducing token consumption by 70.53% compared with the prior most efficient method. Our framework displays high generalization over different backbones, from open-source, lightweight models to the latest commercial models. Additional case studies on quantitative finance analytics and complex multi-relational SQL workloads further demonstrate the framework's robustness, scalability, and practical applicability in real-world analytical scenarios.
