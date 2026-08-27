# MetaSieve: Faster Relational Deep Learning through SQL-Based Metapath Selection

- arXiv ID: `2608.25903v1`
- Authors: Fahim Shahriar Khan, Ashraf Aboulnaga
- Published: 2026-08-26
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2608.25903v1) | [pdf](https://arxiv.org/pdf/2608.25903v1)

## Abstract

Relational Deep Learning (RDL) is an effective approach to machine learning over multi-table relational databases. In RDL, a database is modeled as a graph in which each row is a node and each foreign-key relation is an edge, and a graph neural network (GNN) is trained on this graph. Training a GNN requires sampling a subgraph around every seed node in the training set, and the cost of training is largely determined by the size of these subgraphs. This paper aims to reduce subgraph size by leveraging the join and aggregation capabilities of relational database systems. We observe that sampled subgraphs are obtained by following metapaths composed of foreign-key links, and that many of these metapaths can be pruned without loss of accuracy. We present MetaSieve, a metapath selection layer that determines which metapaths to retain and which to prune. For each candidate metapath extension, MetaSieve computes statistics via SQL join and aggregation queries and evaluates the extension based on a novel scoring function that prefers lightweight but informative candidates. Metapaths whose scores fall below a threshold are deemed uninformative and pruned. Metapath selection in MetaSieve is lightweight since it relies only on database statistics and task labels, and it is independent of GNN parameters, so it integrates with diverse GNN architectures for classification and regression. Our evaluation on the RelBench benchmark with multiple GNN backbones shows that MetaSieve consistently reduces per-epoch training time by large margins while maintaining and often improving accuracy.
