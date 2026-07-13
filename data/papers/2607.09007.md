# Benchmarking Large Language Models on Repairing Qiskit Programs using Bugs4Q

- arXiv ID: `2607.09007v1`
- Authors: Saumya Brahmbhatt, Mitali Hukkeri, Dongchan Kim, M. V. Panduranga Rao, Lei Zhang
- Published: 2026-07-10
- Primary category: `cs.SE`
- Categories: `cs.SE`, `quant-ph`
- Links: [abs](http://arxiv.org/abs/2607.09007v1) | [pdf](https://arxiv.org/pdf/2607.09007v1)

## Abstract

In quantum programs, Bugs4Q is a widely used benchmark containing real quantum defects. However, its evaluation assumes that benchmark labels remain valid and that generated fixes execute in the target environment. We evaluate two Bugs4Q versions containing 67 unique real Qiskit defects, adding executable tests where missing, and re-run all entries across six pinned Qiskit releases (0.25.0, 0.45.0, 1.0.0, 1.1.1, 2.0.0, and 2.3.1). We find that quantum benchmarks can suffer from silent label inversion: entries become invalid without errors when reference fixes stop executing or buggy programs no longer reproduce failures. Thus, correctness depends on the (benchmark, version) pair rather than the benchmark alone. We evaluate four LLMs (GPT-4o-mini, GPT-5o-mini, GPT-5.4, and GPT-5.4-mini), generating up to 10 repair candidates per defect and testing them across all versions. GPT-5.4 achieves the highest pass@10 (48.8%), followed by GPT-5.4-mini (47.3%), GPT-5o-mini (30.3%), and GPT-4o-mini (22.6%). All models perform best on Qiskit 0.45.0 and decline after the Qiskit 1.0 transition. Many failures arise from deprecated or incompatible APIs rather than incorrect repairs, and 64\% of successful repairs occur on entries invalid under the target version. We release a re-validated, version-pinned Bugs4Q benchmark and show that benchmark validation must precede repair evaluation.
