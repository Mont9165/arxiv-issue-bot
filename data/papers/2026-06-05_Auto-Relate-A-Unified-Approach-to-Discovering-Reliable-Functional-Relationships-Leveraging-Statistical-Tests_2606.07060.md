# Auto-Relate: A Unified Approach to Discovering Reliable Functional Relationships Leveraging Statistical Tests

- arXiv ID: `2606.07060v1`
- Authors: Ziyan Han, Yeye He, Shuyuan Kang, Min Xie, Weiwei Cui, Song Ge, Haidong Zhang, Dongmei Zhang, Surajit Chaudhuri, Rui Mao, Jianbin Qin
- Published: 2026-06-05
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.07060v1) | [pdf](https://arxiv.org/pdf/2606.07060v1)

## Abstract

Tables in spreadsheets, computational notebooks, and databases often contain rich inter-column relationships. Yet these relationships are typically implicit and are often lost when tables are exported to standard formats. Recovering them can benefit downstream tasks, including table understanding, data quality improvement, and provenance analysis. However, simply mining relationships that hold on an observed table is insufficient, as many are spurious due to coincidence, redundancy, or limited data diversity. In this paper, we introduce functional relationships (FRs) as a unified notion for inter-column relationships in tables, subsuming arithmetic relationships, string transformations, and functional dependencies. We characterize FR reliability through four complementary criteria: accuracy, atomicity, stability, and integrity. Guided by these criteria, we propose Auto-Relate, a mine-then-verify framework that first generates accurate candidate FRs and then verifies the remaining reliability criteria through a Minimality Test, a Perturbation Test, and an Independence Test, respectively. To further improve efficiency, we develop three optimization strategies, including a group-by lower bound for early rejection, a closed-form speedup for arithmetic FRs, and a binomial bound for statistically guided early termination. We construct a large-scale benchmark suite from 58,679 real-world spreadsheets and relational tables, containing 6,414 ground-truth FRs spanning all three FR types. Extensive experiments against 18 baselines show that Auto-Relate consistently achieves the best performance, with an average PR-AUC of 0.87, 59% higher than the best competing baseline across all settings.
