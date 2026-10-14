# Externalizing Requirement-to-Repair Artifacts as Observable Traces for LLM-Based Program Repair

- arXiv ID: `2609.14913v1`
- Authors: Zewen Tao, Shin-nosuke Ishikawa
- Published: 2026-09-14
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.14913v1) | [pdf](https://arxiv.org/pdf/2609.14913v1)

## Abstract

Repository-level repair requires not only correct patches but also inspectable records that explain how issue requirements are translated into code changes and post-edit evidence. We contribute THEMIS, a stage-aware repair workflow that externalizes this requirement-to-repair process through semantic interpretation, a runtime requirement-code graph, graph-derived Developer guidance, retained repair rationale and patches, and post-edit audit records. A retrospective audit of 300 SWE-bench Lite cases demonstrates that these artifacts provide broad support for cross-stage inspection: a complete Developer rationale is available for 288 cases, and 214 cases (71.3%) retain a complete audited field set connecting the selected stages. The retained records further enable systematic measurement of cross-stage correspondence: target symbols recur in 62.6% of Developer rationales and in 62.8% of patches, rising to 75.8% when related symbols are included. In a paired 100-case comparison, the relational workflow resolves 19 cases versus 9 for the direct same-input condition; because the two conditions also differ in Analyzer output, graph-derived distillation, and Judge records, we report this as preliminary, workflow-level evidence rather than a causal effect of the graph component. Together, these results show that THEMIS makes otherwise implicit requirement-to-repair transitions inspectable, enabling systematic examination of how repair decisions persist, align, and evolve across stages.
