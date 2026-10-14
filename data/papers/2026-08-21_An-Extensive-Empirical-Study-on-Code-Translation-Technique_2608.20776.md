# An Extensive Empirical Study on Code Translation Technique

- arXiv ID: `2608.20776v1`
- Authors: Ruihang Fan, Jiajun Jiang, Xinpeng Wang, Jiateng Fu, Fengjie Li, Jiasi Shen
- Published: 2026-08-21
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2608.20776v1) | [pdf](https://arxiv.org/pdf/2608.20776v1)

## Abstract

Automated code translation is increasingly important for software evolution, yet the relative strengths and limitations of learning-based and large language model (LLM)-based techniques remain insufficiently understood. To address this gap, we conduct a large-scale empirical study comparing representative code translation techniques across methodological paradigms and translation granularities. We evaluate learning-based methods, LLM-based methods, and general-purpose LLMs on multilingual method-level and class-level benchmarks involving multiple programming languages. Our analysis considers executable correctness, code similarity, translation direction, translation granularity, and failure patterns. The results show that LLMs and LLM-based methods generally outperform learning-based methods in method-level correctness, although similarity metrics alone do not reliably reflect functional correctness. Translation direction substantially affects performance, particularly when translating between languages with different type-system characteristics. Class-level translation remains considerably more difficult than method-level translation because it requires preserving global semantics, interfaces, member relationships, and cross-method dependencies. Our error analysis further shows that static semantic errors and logical errors are the primary challenges in existing code translation systems. These findings provide empirical evidence and practical guidance for developing more robust, type-aware, structure-aware, and context-aware code translation techniques.
