# Efficiently Listing Projected Trees, and Equivalence of Listing and Enumeration

- arXiv ID: `2606.02183v1`
- Authors: Karl Bringmann, Nick Fischer, Yanheng Wang
- Published: 2026-06-01
- Primary category: `cs.DS`
- Categories: `cs.DS`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.02183v1) | [pdf](https://arxiv.org/pdf/2606.02183v1)

## Abstract

The subgraph isomorphism problem and its generalizations such as conjunctive queries, where some nodes are projected, are among the most fundamental problems in graph algorithms and database theory. In this paper, we study the listing and enumeration variants of these problems and present two main results.
  (1) We present the first algorithms for enumerating projected trees with polynomial preprocessing time ($\widetilde{O}(n^{17.42})$) and polylogarithmic delay ($\mathrm{polylog}(n)$). Prior to this work, all algorithms in the literature required time $Ω(n^{Ω(k)} + t)$ or $t \cdot n^{Ω(1)}$ to list all copies of a $k$-node tree with projections, where $t$ is the number of solutions. Our result generalizes to arbitrary projected hypergraphs, achieving enumeration in preprocessing time $\widetilde{O}(m^{17.42 \cdot \mathrm{subw}(H)})$ and polylogarithmic delay, where $\mathrm{subw}(H)$ is the submodular width of the pattern hypergraph $H$. We heavily rely on fast (rectangular and output-sensitive) matrix multiplication, which we complement by fine-grained lower bounds indicating that any algorithm beating time $Ω(n^{Ω(k)} + t)$ must rely on fast matrix multiplication.
  (2) As our second main result, we present a generic enumeration-to-listing reduction, establishing that listing and enumeration are equivalent under natural assumptions. For (colored) subgraph isomorphism, our reduction transforms any listing algorithm running in time $O(f(n,m) + t \cdot g(n,m))$ into an enumeration algorithm with preprocessing time $O((f(n,m)+g(n,m)+m) \log^2 n)$ and delay $O(g(n,m))$. We utilize this equivalence as a tool for proving our first main result, and we expect that our generic reduction will find many future applications.
