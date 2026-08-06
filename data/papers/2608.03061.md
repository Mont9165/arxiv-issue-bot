# Scalable Exact Densest P-Partite Subgraph Search in Heterogeneous Information Networks

- arXiv ID: `2608.03061v1`
- Authors: Jiadong Xie, Jiaming Yang, Kangfei Zhao, Jeffrey Xu Yu
- Published: 2026-08-04
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.03061v1) | [pdf](https://arxiv.org/pdf/2608.03061v1)

## Abstract

Heterogeneous information networks (HINs) model typed entities and typed relations, where dense cross-type structures can reveal cohesive semantic patterns such as prolific author-paper-venue groups. Given a query meta-path, the densest P-partite subgraph search (DPpS) problem jointly selects a nonempty vertex set at each typed position and maximizes the number of induced meta-path instances normalized by the geometric mean of the selected set sizes. Existing exact methods solve DPpS by searching over iRM-sets and reducing each fixed-M problem to minimum-cut computations. However, their scalability is limited by the large number of candidate iRM-sets and the high cost of repeatedly solving large auxiliary networks. In this paper, we propose BoxDPpS, an efficient exact approach that reduces both sources of cost. It performs box-level search with safe region pruning, eliminates redundant representations of the same iRM-set, improves early pruning through bounded warm-up, and compresses each fixed-M auxiliary network for exact parametric pseudoflow solving. Experiments on seven real-world datasets show that BoxDPpS preserves the exact DPpS optimum while achieving an average speedup of 27.04x over the state-of-the-art method.
