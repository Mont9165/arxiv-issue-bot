# CAMGen: A Core Change-Aware Multi-View Framework for Commit Message Generation

- arXiv ID: `2610.31552v1`
- Authors: Bo Xiong, Weisheng Chen, Zongen Ren, Yifeng Zhu, Xutian Li, Runbang Yan, Chong Wang, Peng Liang
- Published: 2026-10-22
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.31552v1) | [pdf](https://arxiv.org/pdf/2610.31552v1)

## Abstract

Commit messages help developers understand code changes and support software maintenance. Recent approaches use repository context to improve commit message generation (CMG) with large language models (LLMs). However, existing CMG methods provide limited support for understanding how local edits affect functionality jointly implemented by multiple code entities. This functional understanding is essential for generating commit messages that explain the main change and its impact. To address this problem, we propose CAMGen, a core change-aware multi-view commit message generation framework that incorporates functional context into generation. CAMGen identifies core entities that represent the primary change intent. It then forms candidate functional units through repository-wide semantic clustering and uses those containing the core entities to construct a Functional Semantic View. This view supplies semantic context for interpreting the affected functionality. CAMGen also uses context provided by the Structural Dependency View and the Historical Exemplar View. The context from all three views is then provided to the LLM together with the code diff to guide CMG. The experimental results show that CAMGen outperforms representative CMG baselines across three programming languages. Human evaluation further shows that CAMGen generates more complete commit messages with clearer explanations of change rationale and impact. These results demonstrate the value of functional context and complementary repository information for CMG.
