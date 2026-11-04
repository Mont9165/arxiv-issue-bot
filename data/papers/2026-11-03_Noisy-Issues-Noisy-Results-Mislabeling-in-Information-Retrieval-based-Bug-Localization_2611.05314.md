# Noisy Issues, Noisy Results: Mislabeling in Information Retrieval-based Bug Localization

- arXiv ID: `2611.05314v1`
- Authors: Moumita Asad, Rafed Muhammad Yasir, Yirui He, Ziyao He, Sam Malek
- Published: 2026-11-03
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.05314v1) | [pdf](https://arxiv.org/pdf/2611.05314v1)

## Abstract

Information Retrieval-based Bug Localization (IRBL) leverages bug reports to identify faulty source files. Evaluations of IRBL approaches primarily rely on labeled issues from issue tracking systems. However, prior research has shown that issue labels are frequently incorrect in open-source projects, threatening the validity of IRBL evaluations. Existing studies have primarily examined traditional IRBL techniques on small datasets, overlooking modern approaches and the partial overlap between noisy and cleaned datasets. In this paper, we conduct a large-scale empirical study to investigate the prevalence and impact of mislabeled issues in IRBL benchmarks. We analyze five benchmark datasets comprising over 55,000 issue reports and find that, on average, 34.82% of issues are mislabeled. We further evaluate six IRBL techniques, spanning traditional, deep learning-based, and large language model-based approaches using the widely adopted Ye et al. benchmark and statistical methods that account for dataset overlap. Our results show that removing mislabeled issues from evaluation datasets significantly reduces measured performance across all six techniques, with Mean Reciprocal Rank decreasing by 4.68%-21.74%. Although mislabeling does not change the relative ranking of techniques, it affects the magnitude of their performance differences. These findings highlight the importance of reliable evaluation data for ensuring valid and meaningful comparisons of IRBL techniques.
