# Universal Encoders for Modular Relational Deep Learning

- arXiv ID: `2606.21434v1`
- Authors: Jakub Peleška, Gustav Šír
- Published: 2026-06-19
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.21434v1) | [pdf](https://arxiv.org/pdf/2606.21434v1)

## Abstract

Relational Deep Learning (RDL) models multi-tabular databases as temporal heterogeneous graphs for end-to-end representation learning. While RDL is evolving rapidly, existing approaches face significant generalization obstacles. They are either schema-specific, requiring training from scratch for every new database, or they rely on monolithic architectures that entangle feature encoding with graph message-passing. Analyzing these limitations, we establish four core pillars for building foundational relational models: semantic granularity, structural topology, temporal causality, and unified optimization.
  Addressing these pillars, we propose a modular approach that decouples row encoding from graph message-passing. We introduce the Universal Row Encoder, a transformer-based module that integrates raw cell data with schema metadata$-$including column semantics, table names, and global distribution statistics$-$to produce table-width invariant row embeddings. By explicitly feeding global statistics to an intra-row self-attention mechanism, the encoder natively contextualizes unseen features and handles sparse data. Serving as a flexible "backend" for any downstream graph architecture, our pretrained encoder enhances cross-database knowledge transfer on the established RelBench benchmarks while improving learning convergence and memory footprint.
