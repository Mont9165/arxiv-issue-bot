# ScanTwin: Simulating Performance Regressions Without Access to Tenant Data

- arXiv ID: `2605.29093v1`
- Authors: Donghyun Sohn, Jennie Rogers
- Published: 2026-05-27
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.29093v1) | [pdf](https://arxiv.org/pdf/2605.29093v1)

## Abstract

In cloud data platforms, developers often encounter performance regressions that occur in specific tenant datasets. However, due to confidentiality constraints, they cannot access the original data, which makes it difficult to reproduce these regressions locally. Current methods for synthetic data usually focus on statistical properties, such as matching data distributions or improving query accuracy. However, they overlook the physical properties that control how the engine behaves during scans, including row-group pruning.
  We propose ScanTwin, a lightweight framework that extracts a per-row-group sketch from the Parquet footer, including boundary values and compressed sizes, and releases them under $\varepsilon$-differential privacy using a boundary parameterization. On TPC-H and SSB (6M rows), ScanTwin achieves 0% pruning error and less than 1% byte error at $\varepsilon{=}\infty$. Under $\varepsilon{=}5$, high-selectivity queries ($>$30%) incur below 8.5% pruning error on both datasets, and per-query scan timing on DuckDB closely tracks the original.
