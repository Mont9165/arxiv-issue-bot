# The Decode-Work Law: Margin-Governed, Provably-Exact Spatial Joins over Compressed Geometry

- arXiv ID: `2607.01182v1`
- Authors: Madhulatha Mandarapu, Sandeep Kunkunuru
- Published: 2026-07-01
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.CG`
- Links: [abs](http://arxiv.org/abs/2607.01182v1) | [pdf](https://arxiv.org/pdf/2607.01182v1)

## Abstract

Filter-and-refine spatial joins have always avoided touching exact geometry for certified candidate pairs, but the field never modeled the decompression cost of the pairs that survive the filter. When geometry is stored in a compressed, progressively-decodable multiresolution codec, the join's true cost is bytes decoded. We study provably-exact polygon intersection joins over a Douglas-Peucker level-of-detail (LOD) ladder, certified by a two-sided Hausdorff-margin test, and make two contributions. First, a reproducible mechanism and harness: on real U.S. Census TIGER water polygons, our progressive certificate join returns the exact join result while decoding 3.4-16.8x (median 5.9x) fewer vertices than naive decompress-then-refine, and about 4.9x fewer than the single-approximation multi-step baseline of Brinkhoff et al. (1994), with zero correctness violations (set-equality against a full-precision oracle) across 31 workloads. Second, a characterization we call the decode-work law: decode work is governed by each pair's signed-clearance margin -- how close it is to the predicate-flip boundary -- independent of object size, because the certificate descends the ladder only until its resolution beats the margin. The law is clean on controlled geometry (held-out R2=0.87, size-independent) and directional on real data (R2 ~= 0.55). We are explicit about what does not hold: a near-boundary-vertex predictor is the wrong model (we pre-registered one and rejected it), a selectivity regime forecaster did not materialize, and the worst case is the trivial Omega(v) read bound on adversarially interleaved boundaries. We contribute the mechanism, budget-honest decode accounting, and an open harness; we do not claim a new index.
