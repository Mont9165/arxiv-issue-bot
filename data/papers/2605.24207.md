# Incorporating Deep Learning Design in Database Queries

- arXiv ID: `2605.24207v1`
- Authors: Yuval Lev Lubarsky, Dean Light, Boaz Berger, Shunit Agmon, Benny Kimelfeld
- Published: 2026-05-22
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2605.24207v1) | [pdf](https://arxiv.org/pdf/2605.24207v1)

## Abstract

Deep learning over relational databases is conventionally realized by translating data into graph representations and applying graph-based neural networks within external frameworks. This round-trip between the database and external machine learning (ML) systems introduces non-trivial engineering overhead. In effect, these graph neural networks operate on tuple embeddings and manipulate them in ways that capture the interactions induced by relational joins. Given this natural correspondence, there is no fundamental reason why specifying a neural network over relational data should be substantially harder than querying it. We propose an approach that naturally integrates deep learning with database queries. The key idea is to associate each tuple with provenance, represented as a vector embedding with learnable parameters. Queries are lifted to operate jointly on data and embeddings, mapping input relations with embedded tuples to output relations with embedded tuples. This approach provides a declarative foundation for relational deep learning, facilitating integration with database systems, optimization, and wide adoption.
  We describe RelaNN, a proof-of-concept implementation of this approach built on top of PyTorch and cuDF. We illustrate the utility of RelaNN by implementing various graph-learning models, including graph convolutional networks, heterogeneous graph transformers, hypergraph neural networks and deep homomorphism networks. The simplicity of the programs and their competitive runtime performance demonstrate a concrete path toward making the implementation of state-of-the-art neural networks over databases as simple as writing a query.
