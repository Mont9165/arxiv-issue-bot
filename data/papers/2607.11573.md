# Knowledge-Guided Synthetic Bug Feedback for LLM-Based Unit Test Generation

- arXiv ID: `2607.11573v1`
- Authors: Ziheng Wang, Maike Li, Chen Zhi
- Published: 2026-07-13
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.11573v1) | [pdf](https://arxiv.org/pdf/2607.11573v1)

## Abstract

Large language models (LLMs) have opened new opportunities for unit test generation, but executable tests do not necessarily reveal real defects. This paper studies how historical real-bug mechanisms can be transformed into executable feedback targets for LLM-based unit test generation. The proposed framework constructs structural and semantic representations of real-bug records, retrieves mechanisms applicable to a focal method, and instantiates them as synthetic bugs that guide iterative test enhancement. We evaluate the approach on method-level real-bug detection tasks from Defects4J and show that mechanism-guided synthetic-bug feedback improves real-bug detection over execution-, coverage-, mutation-, knowledge-, and search-based baselines. The results suggest that organizing real-bug mechanisms as retrievable and executable feedback targets is an effective way to guide generated tests toward bug-triggering inputs and behavioral oracles.
