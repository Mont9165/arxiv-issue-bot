# LinkRank: A Learning-to-Rank Framework for One-to-Many Issue-Commit Traceability

- arXiv ID: `2607.23610v1`
- Authors: Abhishek Kumar, Tuhin Mondal, Partha Pratim Das, Partha Pratim Chakrabarti
- Published: 2026-07-26
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.23610v1) | [pdf](https://arxiv.org/pdf/2607.23610v1)

## Abstract

Recovering traceability links between issues and commits is important for software maintenance, debugging, impact analysis, and project understanding. However, most existing approaches assume a one-to-one relationship, where each issue is linked to a single commit. In practice, many issues are resolved through multiple commits, and ignoring this one-to-many nature can lead to incomplete traceability. This paper presents LinkRank, a learning-to-rank framework for recovering one-to-many issue--commit links. Unlike existing methods that mainly judge issue--commit pairs independently, LinkRank considers the set of candidate commits for an issue and identifies the commits that are most likely to contribute to its resolution. To support realistic evaluation, we construct a new dataset from six open-source GitHub repositories. LinkRank follows an iterative pick--remove--renormalize strategy: it selects the highest-ranked commit, removes it from the candidate pool, renormalizes the remaining scores, and repeats the process until the stopping criterion is met. We evaluate LinkRank under two settings: Known-K, where the true number of linked commits is available, and Unknown-K, where the model must infer when to stop selecting commits using ABS and REL stopping rules. Across six projects, LinkRank achieves an average Known-K F1 score of 74.54%, compared with 48.39% for the strongest baseline. In the Unknown-K setting, LinkRank achieves 68.84% F1 with ABS and 67.02% F1 with REL, outperforming the strongest baselines under both automatic stopping rules. Overall, the findings suggest that one-to-many issue--commit traceability is better addressed as an issue-centric ranking and iterative selection problem than as independent pairwise classification.
