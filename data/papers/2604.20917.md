# The Path Not Taken: Duality in Reasoning about Program Execution

- arXiv ID: `2604.20917v1`
- Authors: Eshgin Hasanov, Md Mahadi Hassan Sibat, Santu Karmaker, Aashish Yadavally
- Published: 2026-04-22
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.AI`, `cs.CL`, `cs.PL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.20917v1) | [pdf](https://arxiv.org/pdf/2604.20917v1)

## Abstract

Large language models (LLMs) have shown remarkable capabilities across diverse coding tasks. However, their adoption requires a true understanding of program execution rather than relying on surface-level patterns. Existing benchmarks primarily focus on predicting program properties tied to specific inputs (e.g., code coverage, program outputs). As a result, they provide a narrow view of dynamic code reasoning and are prone to data contamination. We argue that understanding program execution requires evaluating its inherent duality through two complementary reasoning tasks: (i) predicting a program's observed behavior for a given input, and (ii) inferring how the input must be mutated toward a specific behavioral objective. Both tasks jointly probe a model's causal understanding of execution flow. We instantiate this duality in DexBench, a benchmark comprising 445 paired instances, and evaluate 13 LLMs. Our results demonstrate that dual-path reasoning provides a robust and discriminative proxy for dynamic code understanding.
