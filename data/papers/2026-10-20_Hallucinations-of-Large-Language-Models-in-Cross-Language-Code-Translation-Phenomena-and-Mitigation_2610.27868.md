# Hallucinations of Large Language Models in Cross-Language Code Translation: Phenomena and Mitigation

- arXiv ID: `2610.27868v1`
- Authors: Yali Du, Yunji Zhang, Ming Li
- Published: 2026-10-20
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2610.27868v1) | [pdf](https://arxiv.org/pdf/2610.27868v1)

## Abstract

Code translation converts source code from one programming language to another while preserving its functionality. Although Large Language Models (LLMs) have improved code translation, their outputs still contain hallucinations: generated code that conflicts with the source program, violates target-language facts, or introduces contextually inconsistent dependencies. These failures are especially harmful in translation because small semantic deviations can silently change program behavior. Existing hallucination studies mainly focus on natural-language generation or code generation, leaving the forms, distribution, and mitigation of hallucinations in cross-language code translation insufficiently characterized. This paper presents a systematic empirical study of LLM hallucinations in code translation. Across three benchmark datasets, six language pairs, and seven LLMs, we construct a taxonomy with three major categories: Semantic Consistency Conflicts, Factual Knowledge Conflicts, and Project Context Deviations. We manually annotate 13,919 hallucination cases and analyze how hallucination types vary across models, datasets, and language directions. Guided by the taxonomy, we further propose HaluCodeTran, a mitigation framework that combines BM25-based retrieval of relevant translation examples with taxonomy-aware reflective refinement. The study provides an execution-tested characterization of code-translation hallucinations and a practical baseline for building more reliable LLM-based code migration tools.
