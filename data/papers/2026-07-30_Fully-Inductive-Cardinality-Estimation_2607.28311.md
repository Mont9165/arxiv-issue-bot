# Fully Inductive Cardinality Estimation

- arXiv ID: `2607.28311v1`
- Authors: Tim Schwabe, Lukas Ketzer, Maribel Acosta
- Published: 2026-07-30
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2607.28311v1) | [pdf](https://arxiv.org/pdf/2607.28311v1)

## Abstract

Query optimization of Basic Graph Patterns (BGP) SPARQL queries over Knowledge Graphs (KG) requires accurate cardinality estimation. Recently published learned estimators outperform statistics- and sampling-based approaches, but share a limitation preventing their adoption in real-world triplestores: they are transductive and require retraining when the underlying graph changes or when applied to new graphs. We present FICE (Fully Inductive Cardinality Estimation), the first learned cardinality estimator for BGP queries over KGs that generalizes to entirely unseen graphs (including unseen relations), without any retraining. FICE is a graph neural network (GNN) with two coupled components. First, an encoder GNN over a factor-graph view of the KG produces entity and relation embeddings. We prove that BGP cardinality is a local function of the 2-hop neighborhood around bound terms in this view, motivating the local message-passing encoder. A decoder GNN then composes these embeddings along the join topology of the query to predict log-cardinality. The encoder and decoder are trained jointly, making the embeddings specialized for cardinality estimation. FICE is trained using neighborhood sampling to scale to KGs with millions of triples, and decouples embedding generation from cardinality decoding to enable estimation latency below a millisecond. Compared to learned and non-learned baselines over 10 KGs, FICE reduces the overall median q-error from 13.54 (for the best competitor) to 5.34 and dominates all approaches in tail behavior.
