# The Power of Bidegeneracy for Hypergraph Data Structures

- arXiv ID: `2611.04900v1`
- Authors: Marco Bressan, Stefano Clemente, Giacomo Fumagalli, Daniel Paul-Pena, C. Seshadhri
- Published: 2026-11-03
- Primary category: `cs.DS`
- Categories: `cs.DS`, `cs.DB`, `cs.DM`
- Links: [abs](http://arxiv.org/abs/2611.04900v1) | [pdf](https://arxiv.org/pdf/2611.04900v1)

## Abstract

A hypergraph $H = (V,E)$ describes a set system over a vertex universe $V$. Hypergraphs are increasingly popular in network science, as they represent interactions between subsets of vertices. A natural challenge is to design a data structure for $H$ to quickly answer basic questions about it, e.g. how many neighbors a vertex $v$ has or whether a hyperedge contains a vertex subset $S$. Such questions are trivial for graphs, for which we simply inspect the adjacency list. The gold standard, from a data structures perspective, would be near-linear time preprocessing and query answering in (poly)logarithmic time. Since this is unlikely for arbitrary $H$, we ask for well-motivated hypergraph properties that can make such a goal possible.
  We introduce bidegeneracy, a measure of hypergraph sparsity that strictly generalizes many other measures, including bounded degree, bounded rank, and bounded $\infty$-degeneracy. We show that bounded bidegeneracy yields fast hypergraph data structures. For a large set of fundamental queries, including their listing and sampling versions, we obtain near-linear preprocessing and (poly)logarithmic query time. Moreover, direct reductions from assumptions like the Orthogonal Vectors Conjecture suggest that, without assumptions on the input, these structures require almost-quadratic preprocessing or almost-linear query time.
  We use bidegeneracy to compute a compressed representation of $H$ and perform careful reductions to stabbing and searching problems in $\mathbb{R}^d$. Our framework significantly extends the well-studied "partial matching" problem of finding database entries through wildcard search. It also uncovers an intriguing connection between hypergraph sparsity, compression, and the complexity of hypergraph primitives. We also find remarkably low bidegeneracy in hypergraph datasets from the literature, suggesting practical consequences.
