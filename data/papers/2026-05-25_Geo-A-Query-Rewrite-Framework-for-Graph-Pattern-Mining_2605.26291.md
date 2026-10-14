# Geo: A Query Rewrite Framework for Graph Pattern Mining

- arXiv ID: `2605.26291v1`
- Authors: Nazanin Yousefian, Kasra Jamshidi, Keval Vora, Anders Miltner
- Published: 2026-05-25
- Primary category: `cs.PL`
- Categories: `cs.PL`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.26291v1) | [pdf](https://arxiv.org/pdf/2605.26291v1)

## Abstract

Graph pattern mining is important for analyzing graph data. Graph mining systems typically require answering pattern matching queries, which involve solving the NP-complete subgraph isomorphism problem. To address this, domain experts often develop custom optimization strategies based on exploiting substructural similarities across different patterns. While these optimizers can be effective, their development is challenging, limiting the exploration of interactions between different optimization strategies and restricts experts from continuously improving the optimizers -- such as by incorporating additional custom or general pattern-based equivalences over time.
  We present a programmable pattern matching query optimizer called Geo, which automatically manages the interactions between various equivalences, ensures the optimizations maintain correctness of results, and simplifies the management of substructure equivalences. Geo exposes a simple but flexible language for expressing pattern equivalences as rewrite rules. By maintaining canonical representations of generated patterns during equality saturation, Geo avoids issues arising from syntactic differences in isomorphic patterns. Additionally, we develop embedded reconstructablility (EmRec) that tracks provenance across equivalences to ensure various reconstructability needs of desired outputs. Our evaluation demonstrates that Geo can discover novel query equivalences through complex composition of various rewrite rules, enabling our optimized queries to achieve a cost reduction of up to 99% compared to the queries in prior work. We further test Geo's effectiveness at speeding up practical graph mining problems by using it in two representative case studies -- approximate pattern matching and quasi-clique mining, and find it is highly effective at optimizing these tasks, enabling cost reductions of up to 71%.
