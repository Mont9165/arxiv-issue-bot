# An Empirical Evaluation of Locally Deployed LLMs for Bug Detection in Python Code

- arXiv ID: `2604.23361v1`
- Authors: Jelena Ilić Vulićević
- Published: 2026-04-25
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2604.23361v1) | [pdf](https://arxiv.org/pdf/2604.23361v1)

## Abstract

Large language models (LLMs) have demonstrated strong performance on a wide range of software engineering tasks, including code generation and analysis. However, most prior work relies on cloud-based models or specialized hardware, limiting practical applicability in privacy-sensitive or resource-constrained environments. In this paper, we present a systematic empirical evaluation of two locally deployed LLMs, LLaMA 3.2 and Mistral, for real-world Python bug detection using the BugsInPy benchmark. We evaluate 349 bugs across 17 projects using a zero-shot prompting approach at the function level and an automated keyword-based evaluation framework. Our results show that locally executed models achieve accuracy between 43% and 45%, while producing a large proportion of partially correct responses that identify problematic code regions without pinpointing the exact fix. Performance varies significantly across projects, highlighting the importance of codebase characteristics. The results demonstrate that local models can identify a meaningful share of bugs, though precise localization remains difficult for locally executed LLMs, particularly when handling complex and context dependent bugs in realistic development scenarios.
