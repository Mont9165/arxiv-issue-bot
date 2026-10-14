# Modeling and Optimization for Massive Data Allocation in Database

- arXiv ID: `2605.31002v1`
- Authors: Panpan Niu, Boxiang Ren, Hao Wu, Xin Yao
- Published: 2026-05-29
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.31002v1) | [pdf](https://arxiv.org/pdf/2605.31002v1)

## Abstract

In the era of big data, e-commerce and Internet platforms face the challenge of processing massive amounts of data. However, due to data being scattered across different machines in distributed database, extra communication costs are incurred in gathering relevant data to complete transactions. Without a carefully designed data placement scheme, this cost can severely impact the performance of Online Transaction Processing systems. To meet industry requirements, algorithms that output a data placement scheme that achieves i) data balance and ii) low communication overhead within a fixed period of time are eagerly investigated. Although some existing methods have been studied, they do not adequately meet the aforementioned requirements. In this paper, inspired by the normalized cut of spectral clustering, we introduce a novel model for data allocation problem. The normalized cut reconciles the inherent conflict between the two objectives. Taking into account the variable characteristics of the model, we formulate the problem as a 0-1 optimization problem, and solve the relaxed problem using the Bregman proximal gradient method with guaranteed convergence. The numerical experiments reveal that the convergent solutions can be smoothly rounded to discrete solutions. Furthermore, our algorithm surpasses both simple and meta-heuristic partitioning schemes by minimizing migration costs while maintaining a superior balance.
