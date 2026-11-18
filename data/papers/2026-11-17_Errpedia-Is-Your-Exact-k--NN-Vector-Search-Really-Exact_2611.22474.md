# Errpedia: Is Your Exact $k$-NN Vector Search Really Exact?

- arXiv ID: `2611.22474v1`
- Authors: Yinuo Deng, Ying Zhang, Hanchen Wang, Wenjie Zhang
- Published: 2026-11-17
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.22474v1) | [pdf](https://arxiv.org/pdf/2611.22474v1)

## Abstract

Exact $k$-nearest-neighbor ($k$-NN) vector search is a common feature of vector libraries and database systems. It serves applications that require exact results and provides the ground truth for evaluating approximate search. However, floating-point rounding and overflow can cause an exact search to return mathematically incorrect top-$k$ result sets. These errors can go unnoticed and affect downstream tasks that rely on exact results. We present Errpedia, a purpose-built dataset for testing the numerical correctness of exact vector search. Errpedia contains 1,616 queries across 21 error categories, with ground truth independently verified using exact rational arithmetic. We evaluate 20 widely used library and database configurations and find that every tested configuration returns mathematically incorrect top-10 result sets on at least 1 applicable query. Failures include misranking nearly equidistant vectors and returning incomplete results: 1 library omits all 10 exact matches to a query, and several systems return fewer than $k$ neighbors. We release Errpedia as a reproducible benchmark for developers and researchers to test their implementations. The dataset is publicly available at https://github.com/dynos01/errpedia.
