# Corporate-Family Resolution Is Not a String-Matching Problem: A Public Benchmark Stratified by Name Visibility

- arXiv ID: `2609.04269v1`
- Authors: Harshit Gupta
- Published: 2026-09-02
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.IR`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2609.04269v1) | [pdf](https://arxiv.org/pdf/2609.04269v1)

## Abstract

Deciding whether two supplier records belong to the same corporate family is a prerequisite for spend consolidation, credit exposure aggregation and sanctions screening. It is usually treated as entity matching, but the tasks differ: a family link connects records that are deliberately different entities, and the evidence often appears in neither record. We introduce CorpFam, a public benchmark of 54,864 candidate pairs over 10,307 corporate families, derived from 6,638,350 US federal award records in which every supplier self-reports its ultimate parent to a government registry. Pairs are stratified by name visibility: whether the names are identical after normalisation, share a distinctive token, or share none. Because strata have positive rates from 10.2% to 97.3%, we report per-stratum recall, base-rate invariant, rather than F1, which is not. The strongest of 5 matchers recovers 100.0% of identical pairs and 4.2% of invisible ones; no method exceeds 4.7% on the latter. The failure begins before matching. Blocking decides which pairs a matcher sees, and we evaluate 7 schemes spanning phonetic keys, attribute keys that ignore the name, and semantic nearest neighbours. None reaches three percent on invisible pairs, and their union recovers 6.8%. 93.2% of these links never enter the candidate set, so no matching-stage improvement can reach them. The links are real: against SEC Exhibit 21 subsidiary schedules, which share no provenance with procurement registration, 64.2% of invisible links are corroborated, against 0.16% under permuted parents and 0.41% against the same parent's wrong exhibit: two unrelated nulls agreeing to within 0.25 points. Corporate-family resolution is a retrieval problem misfiled as a matching problem; the intervention point is candidate generation, not ranking. The benchmark, adjudication log, and code reproducing every number are released.
