# Can Aggregate Invariants Accelerate Continuous Subgraph Matching? Limits, Laws, and a Dynamic Spectral Index

- arXiv ID: `2606.24421v1`
- Authors: Minghao Chen, Jiale Zheng
- Published: 2026-06-23
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.DB`, `cs.DS`
- Links: [abs](http://arxiv.org/abs/2606.24421v1) | [pdf](https://arxiv.org/pdf/2606.24421v1)

## Abstract

Spectral filtering recently delivered substantial pruning for \emph{static} subgraph matching: Laplacian interlacing rejects candidates whose neighborhoods cannot host the query. We study whether such aggregate structural tests can accelerate \emph{continuous} subgraph matching (CSM) over dynamic graphs, and answer in three parts. First, lazily maintained spectral bounds are infeasible exactly where spectral pruning has value: we characterize the tightest safe rule over a formalized perturbation relaxation and show that even it loses essentially all pruning power within four touching updates. Second, exact maintenance is affordable when selective: pruning utility and recomputation cost are anti-correlated across vertices -- hubs provably never prune -- so recomputing small-neighborhood spectra on touch sustains exact local spectra at microseconds per update, complete by construction. Third, integrated into a decoupled CSM benchmark against an identical-minus-spectra control, the tests remove up to $51\%$ of candidates or safely skip up to $47\%$ of update enumerations, yet enumeration intermediates remain unchanged -- beyond the gates' skipped first-level bindings, typically zero -- across two engines, four real graphs, two stream types, and $77$ solved queries; a constructed radius-stratified workload confirms the instrument detects the exception when one exists ($-99.9\%$ intermediates, $748\times$ faster). Aggregate tests accelerate what scales with candidate sets -- construction, list scans -- never adjacency-guided exploration. We distill an intermediate-invariance methodology for evaluating CSM filters and release a reusable dynamic local-spectra index.
