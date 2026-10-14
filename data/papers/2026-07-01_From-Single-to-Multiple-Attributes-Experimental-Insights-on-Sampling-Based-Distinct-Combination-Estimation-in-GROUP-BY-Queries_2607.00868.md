# From Single to Multiple Attributes: Experimental Insights on Sampling-Based Distinct Combination Estimation in GROUP-BY Queries

- arXiv ID: `2607.00868v1`
- Authors: Yujie Zhang, Xiaochun Yang, Bin Wang, Yuan Sui
- Published: 2026-07-01
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.00868v1) | [pdf](https://arxiv.org/pdf/2607.00868v1)

## Abstract

Estimating the number of distinct combinations in multi-attribute GROUP-BY queries remains a significant yet underexplored challenge. Current cardinality estimation techniques primarily focus on SPJ queries (i.e., selections, projections, and joins) and neglect GROUP-BY operations; meanwhile, distinct value estimation research has mainly targeted the single-attribute setting. Although sampling-based methods, including recent approaches with learned models, can theoretically support multi-attribute estimation, their practical effectiveness remains unclear. A comprehensive empirical evaluation is thus lacking to address whether joint distribution information from samples alone is sufficient for accurate multi-attribute estimation, whether existing methods fully exploit single-attribute information and can be further optimized, and whether filtered GROUP-BY queries can be accurately estimated. To this end, we propose a specialized workload generator for multi-attribute GROUP-BY queries and generate both filtered and non-filtered queries over four real-world datasets. By evaluating existing methods across synthetic workloads and the multi-table TPC-H benchmark, we analyze the sources of GROUP-BY cardinality estimation errors and their impact on PostgreSQL's plan selection, offering key recommendations for future estimator design.
