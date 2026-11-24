# AEGIS: Evidence-Guided Set Decisions for Requirement-to-Code Traceability

- arXiv ID: `2611.30093v1`
- Authors: Zhiyao Wang, Yiming Peng, Munan Li, Mingyue Zhang, Guanghong Li, Jialong Li, Tatsuhiro Tsuchiya
- Published: 2026-11-23
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.30093v1) | [pdf](https://arxiv.org/pdf/2611.30093v1)

## Abstract

Requirement-to-code traceability recovery identifies code artifacts that implement a requirement, but manual review costs limit how many candidates developers can inspect. Code relations can reveal candidates missed by textual retrieval, yet can also introduce code unrelated to the requirement. We propose AEGIS, which combines retrieval evidence and code relations to construct and revise trace sets under a project-wide review budget. Grouped retrieval and semantic retrieval supply candidates. A set objective combines relevance to the requirement with structural compatibility. Local search constructs sets of different sizes, and dynamic programming selects one set per requirement within the budget. Call-context admission then compares replacements using evidence from arguments and return values in calls involving protected members, while bounding retrieval-score loss. Across 13 projects, AEGIS achieves the highest project-macro average on nine of ten evaluation metrics among the compared methods. Relative to same-corpus adaptations of TAROT-VSM and FTLR+MC, it improves F$_1$@5 by 33.21% and 52.28%, and MAP by 38.58% and 49.08%, respectively.
