# Self-Spec Verifiable Code Generation

- arXiv ID: `2609.39568v1`
- Authors: Jiaru Qian, Yihong Dong, Yongmin Li, Hao Zhu, Bin Gu, Ge Li
- Published: 2026-09-30
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.39568v1) | [pdf](https://arxiv.org/pdf/2609.39568v1)

## Abstract

Large language models (LLMs) may generate unreliable code on corner cases missed by testing, while formal verification can provide machine-checkable guarantees. Recently, researchers have proposed several benchmarks to evaluate the capabilities of LLMs in generating formally verifiable code, where LLMs need to formulate formal specifications, generate the corresponding code, and verify its correctness. However, existing benchmarks have two key limitations: (I) They primarily evaluate specification and code generation stage-wise, with code generation typically conditioned on an oracle specification. This setup overlooks whether strong stage-wise performance translates into end-to-end success. (II)They mainly focus on a single proof-oriented language and mathematically structured tasks, offering limited coverage of tasks common in software development. In this paper, we introduce VeriCodeBench, a benchmark for self-spec verifiable code generation, where the LLM relies solely on its own generated specification and code throughout the entire process. VeriCodeBench contains 400 language-native problems across C, Java, Rust, and Python, covering practical concerns in software development. We evaluate specification coverage, code validity, and joint problem-level success. We further introduce CodeNova to enhance the capabilities of LLMs in self-spec verifiable code generation. CodeNova makes requirements explicit through constraint-guided specification and uses verifier feedback to guide targeted implementation repairs. Experimental results reveal that self-generated specifications remain a major bottleneck, while providing more sophisticated specifications may not necessarily lead to higher verification success rates. CodeNova substantially improves performance across all evaluation metrics, enabling Claude Sonnet 5 to achieve the strongest results under the self-spec protocol.
