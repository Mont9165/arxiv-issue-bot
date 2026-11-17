# From Language-Specific to Cross-DSL: Semantic-Role-Guided Model Completion with LLMs

- arXiv ID: `2611.18952v1`
- Authors: Meriem Ben Chaaben, Théo Giraudet, Benoit Combemale, Houari Sahraoui
- Published: 2026-11-13
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2611.18952v1) | [pdf](https://arxiv.org/pdf/2611.18952v1)

## Abstract

The rapid emergence of large language models (LLMs), trained on vast and diverse corpora, has positioned them as a promising source of domain knowledge to assist modelers. However, leveraging LLMs for model completion remains challenging: suggestions must respect both the syntax of a domain-specific language (DSL) and the intended domain semantics, while remaining consistent with an evolving model. This paper presents RAFiC, an LLM-based approach for iterative domain model completion that generalizes across DSLs. It drives completion using metamodel information to ensure syntactic validity and enriches prompts with semantic-role annotations to better capture the intended modeling role of DSL elements. The approach provides context-aware, incremental guidance during model construction. We evaluate RAFiC through an ablation-based comparative study over three DSLs and two scenarios per DSL to isolate the contribution of syntactic and semantic guidance. Across these six scenarios, semantic role guidance improves contribution rate in every case, and RAFiC improves completion effectiveness over weaker prompting configurations in most of them. The largest gains occur for DSLs that are less represented in LLM training data. In these cases, iterative guidance leads to earlier and more stable accepted suggestions, while semantic role guidance improves their relevance.
