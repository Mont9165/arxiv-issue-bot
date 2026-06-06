# Workload acceleration by optimizing materialized view selection using local search

- arXiv ID: `2606.03772v1`
- Authors: Kaina Anderson, Yohanes Yohanie Fridelin Panduman, Yuya Sasaki, Makoto Onizuka
- Published: 2026-06-02
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.03772v1) | [pdf](https://arxiv.org/pdf/2606.03772v1)

## Abstract

The growing size of database workloads has made view selection a key performance challenge. Materializing frequent sub-queries in workloads improves query efficiency, but it incurs significant view maintenance costs due to updates. Although existing methods such as BIGSUBS address this trade-off between the benefit of using materialized views and the overhead of view maintenance, they have two drawbacks: insufficient maintenance cost modeling and ineffective view selection due to probabilistic techniques. We propose a novel view selection method that incorporates incremental view maintenance cost directly into the optimization objective of an integer linear program and applies local search to efficiently explore the solution space. In order to apply local search to the view selection problem, we develop neighboring solutions using sub-query containment, and select initial solutions based on sub-query frequency, utility, or utility per storage unit. Experiments using Redbench, a benchmark simulating real-world query workloads on Amazon Redshift, show that our approach outperforms BIGSUBS in both optimization utility and the quality of selected views.
