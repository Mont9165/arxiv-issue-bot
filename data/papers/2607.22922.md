# iFVS: Towards Instance-Optimized Filtered Vector Search

- arXiv ID: `2607.22922v1`
- Authors: Abdullah Al-Mamun, Yeasir Rayhan, Walid G. Aref
- Published: 2026-07-24
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.22922v1) | [pdf](https://arxiv.org/pdf/2607.22922v1)

## Abstract

Filtered vector search (FVS) is increasingly important in modern AI + DB systems, where vector similarity search is combined with relational predicates. Quantization plays a vital role in these systems by enabling query processing over large vector datasets. However, lossy approaches, e.g., Product Quantization (PQ), incur a precision penalty during distance calculation, thereby negatively impacting the query recall performance. This problem becomes more challenging in FVS because the relevant vector space can change with the relational predicate and selectivity. Motivated by the success of instance-optimized database system components, we introduce iFVS, an Instance-Optimized Filtered Vector Search technique. Given a fixed, quantized vector dataset, and a representative workload of filtered vector queries, iFVS adopts a query-specific codebook generation approach for FVS that is instance-optimized towards a certain dataset and query workload. Instead of using a fixed codebook for all queries, iFVS conditions distance estimation on both the query vector and the filter predicate. This enables more accurate ranking over compressed vectors while preserving compact per-vector storage. Experiments show that iFVS improves the Queries Per Second (QPS)-recall tradeoff across several filter selectivity bins compared with fixed-codebook quantized FVS baselines.
