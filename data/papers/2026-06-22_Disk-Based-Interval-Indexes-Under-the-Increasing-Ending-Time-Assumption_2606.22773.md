# Disk-Based Interval Indexes Under the Increasing Ending Time Assumption

- arXiv ID: `2606.22773v1`
- Authors: Kai Wang, Moin Hussian Moti, Dimitris Papadias
- Published: 2026-06-22
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.22773v1) | [pdf](https://arxiv.org/pdf/2606.22773v1)

## Abstract

Indexes for large collections of intervals are common in temporal databases, where each record has a lifespan, or validity interval. Despite their conceptual differences, we demonstrate that interval indexes can be captured by some corner structure in a 2D space. This representation facilitates the optimization of query processing by identifying nodes that must contain query results versus nodes that may contain results. In addition, we explore the assumption that intervals arrive in order of increasing ending time (IET) to develop disk-based indexes that have compact size, efficient insertions, and fast query processing. Specifically, we first develop CEB, an index in the corner space defined by the interval center and endpoint. Our second contribution is TIDE, which organizes intervals by their duration and endpoint. CEB and TIDE adopt a two-layer architecture, where the leaf nodes of a top tree (ordering intervals by their center or duration) correspond to the root nodes of bottom trees, ordering intervals by their endpoints. Both top and bottom trees are append-only B+-trees to facilitate fast insertions. CEB and TIDE outperform state-of-the-art competitors in terms of index size and insertion speed. In addition, TIDE is always faster in query processing, sometimes by orders of magnitude.
