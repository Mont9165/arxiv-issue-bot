# SEDCoT: Enhancing LLM-Based COBOL Code Translation via Symbolic Execution and Delta Debugging

- arXiv ID: `2607.04092v1`
- Authors: Phillip Entin, Wenchao Gu, Alexander Knapp, Chunyang Chen
- Published: 2026-07-05
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.04092v1) | [pdf](https://arxiv.org/pdf/2607.04092v1)

## Abstract

COBOL remains critical across banking, insurance, and government infrastructure. However, maintenance is increasingly challenging due to outdated technologies, sparse documentation, and developer retirement, necessitating code translation into modern languages like C. Traditional rule-based transcompilers yield outputs that are difficult to read and maintain, while general-purpose large language models (LLMs) achieve suboptimal correctness because COBOL is a low-resource language with distinct logic patterns. To bridge this gap, we propose SEDCoT, a novel COBOL-to-C translation framework. SEDCoT first leverages LLMs for initial translation, then combines symbolic execution with LLM guidance to generate test suites and iteratively repair semantic discrepancies. Finally, it integrates delta debugging to minimize failing tests into succinct counterexamples, accelerating automated code repair. Evaluating SEDCoT on a public COBOL-to-C dataset demonstrates that it outperforms state-of-the-art baselines by at least 12% while producing translations with substantially higher readability than rule-based alternatives.
