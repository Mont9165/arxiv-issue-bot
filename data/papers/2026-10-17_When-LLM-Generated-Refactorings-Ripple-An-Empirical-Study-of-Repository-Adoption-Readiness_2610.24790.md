# When LLM-Generated Refactorings Ripple: An Empirical Study of Repository Adoption Readiness

- arXiv ID: `2610.24790v1`
- Authors: Muhammad Waseem, Aakash Ahmad, Pekka Abrahamsson
- Published: 2026-10-17
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2610.24790v1) | [pdf](https://arxiv.org/pdf/2610.24790v1)

## Abstract

Large Language Models (LLMs) are increasingly used to refactor source files, but file-local evaluations do not reveal changes to contracts, dependencies, or caller assumptions affecting repository adoption. To address this gap, we conduct 1,500 generation attempts across 150 production files from 15 open-source Java repositories, five LLM configurations, and two dependency-aware generation conditions: single-prompt refactoring and LangGraph-based multi-agent refactoring. Of these attempts, 1,455 yield complete candidates eligible for analysis. We evaluate these candidates using local changes, repository-facing structural indicators, detected caller impact, the behavioural-equivalence indicator, and available test evidence, and categorize them as Low-risk, Review-needed, High Contract/Dependency Risk, or Inconclusive. The results show that 1,365 candidates (93.8%) are classified as High Contract/Dependency Risk, whereas 106 (7.3%) have at least one detected broken downstream caller and 290 (19.9%) have a false behavioural-equivalence indicator; only eight satisfy the Low-risk criteria. Within the reason-covered subset, the High-risk rate decreases under more conservative dependency-delta thresholds, while 60 of the 65 candidates with conclusive targeted-test outcomes pass, including 50 classified as High risk. Paired analyses of 705 complete pairs identify no statistically significant generation-condition difference in the principal risk indicators, although model configurations differ in specific detected risk channels. These findings suggest that practitioners should treat LLM-generated refactorings as candidates requiring staged repository-level verification, while future research should validate screening and extraction precision and strengthen compilation, behavioural, and coordinated multi-file verification.
