# Polars inside Intel SGX2 Enclaves: An Empirical Study of Confidential Analytical Query Processing

- arXiv ID: `2605.21797v1`
- Authors: Wei Wang, Burns Smith, Kenny Leftin
- Published: 2026-05-20
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.21797v1) | [pdf](https://arxiv.org/pdf/2605.21797v1)

## Abstract

Trusted Execution Environments (TEEs) have renewed interest in confidential analytics, but most prior evaluations focus on SQL database engines or earlier SGX generations. This paper studies an Arrow-native DataFrame engine, Polars, running inside Intel SGX2 enclaves via Gramine on TPC-H SF30 with Azure Blob Storage. We report both the standard TPC-H power score and a query-only variant that removes table-loading time in order to separate compute overhead from data-ingestion overhead. Across four dataset-width configurations (approximately 22-73 GB), end-to-end overhead remains nearly constant at 1.49-1.56$\times$, but this composite metric obscures two distinct behaviors: query-only overhead declines from 1.51-1.52$\times$ to 1.43-1.44$\times$, whereas table-loading overhead rises from 2.27$\times$ to 4.07$\times$. We further show that overhead is not uniform across queries: for the len130 configuration, the median per-query SGX slowdown is 1.45$\times$ with a maximum of 2.57$\times$, and a small set of queries exhibits pronounced run-to-run spikes consistent with stateful EPC pressure. Finally, we compare Polars' lazy and eager APIs under the same TEE setting. Lazy execution is 2.25-2.27$\times$ faster overall, while eager execution fails with out-of-memory errors at 41 GB and above. Relative to the recent DuckDB-SGX2 study, our results suggest that SGX2 can support Arrow-native analytical processing with a similar order of security overhead, but that load-path amplification and API-level optimization are first-order determinants of end-to-end performance.
