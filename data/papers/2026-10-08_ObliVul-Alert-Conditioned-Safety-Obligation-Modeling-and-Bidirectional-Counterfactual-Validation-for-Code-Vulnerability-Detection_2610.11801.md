# ObliVul: Alert-Conditioned Safety Obligation Modeling and Bidirectional Counterfactual Validation for Code Vulnerability Detection

- arXiv ID: `2610.11801v1`
- Authors: Heyang Tan, Chengxin Gao, Xin Wen, Jiaxin Li, Rui Cao
- Published: 2026-10-08
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.11801v1) | [pdf](https://arxiv.org/pdf/2610.11801v1)

## Abstract

In real-world software development, the primary challenge in vulnerability detection is often not finding suspicious code, but identifying which alerts among the large number of candidate alerts produced by static analysis truly warrant attention. Existing learning-based methods mainly identify suspicious patterns at the function or line level, making it difficult to extract complete program evidence centered on an individual alert. Although large language models can infer risk sources, dangerous operations, protection conditions, and state preconditions from local program facts, such semantic information cannot be reliably aligned with specific program nodes, dependency relations, and propagation paths, and is therefore insufficient to verify whether the corresponding safety obligations truly affect the current alert. To address this problem, we propose ObliVul, an alert-conditioned safety obligation modeling and bidirectional counterfactual validation framework for vulnerability detection. For each candidate alert, ObliVul first extracts a Local Evidence Pack (LEP) from the Code Property Graph (CPG) and uses a large language model to recover candidate safety obligations. It then aligns the safety obligations with program nodes, dependency edges, and path scopes to construct a Local Safety Obligation Graph (LSOG). Finally, VAFI aggregates complementary verified alert evidence while suppressing redundant or weaker evidence to produce a function-level vulnerability prediction. Experimental results show that ObliVul effectively distinguishes vulnerable versions from fixed versions and reduces persistent false positives on fixed code. Ablation studies further confirm the necessity of each component for safety obligation recovery, risk response validation, and function-level vulnerability inference.
