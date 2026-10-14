# Expressive Power of Deep Homomorphism Networks over Relational Databases

- arXiv ID: `2605.22852v1`
- Authors: Moritz Schönherr, Balder ten Cate, Maurice Funk, Benny Kimelfeld, Carsten Lutz, Arie Soeteman
- Published: 2026-05-18
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`, `cs.LG`, `cs.LO`
- Links: [abs](http://arxiv.org/abs/2605.22852v1) | [pdf](https://arxiv.org/pdf/2605.22852v1)

## Abstract

The expressive limitations of message-passing Graph Neural Networks (GNNs) have motivated a wide range of more powerful graph learning architectures. We advocate Deep Homomorphism Networks (DHNs) as a model particularly well-suited for learning over relational databases, due to their close connection to important fragments of SQL such as conjunctive queries. We study the precise expressive power of DHNs by relating them to various natural fragments and extensions of first-order logic (FO). For DHNs with max, sum, and mean aggregations, we establish connections to the unary negation fragment (UNFO) and to the extensions of UNFO with counting quantifiers and with ratio quantifiers. We further relate sum-aggregation DHNs to the unary quantifier alternation fragment of FO and to an extension of FO with expressive counting. Through the classical correspondence between FO and SQL, these results also illuminate the relation between DHNs and SQL. They also enable us to study the decidability of two fundamental static analysis problems for DHNs, the emptiness problem and the subsumption problem. Finally, we confirm through experiments that the established differences in expressive power are reflected in the performance on suitable prediction tasks.
