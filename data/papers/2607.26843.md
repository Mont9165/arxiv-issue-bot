# When Knowledge Changes: Metamorphic Testing of RAG Systems with Mutations

- arXiv ID: `2607.26843v1`
- Authors: Jinhan Kim, Samuele Pasini, Paolo Tonella
- Published: 2026-07-29
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.26843v1) | [pdf](https://arxiv.org/pdf/2607.26843v1)

## Abstract

Retrieval-Augmented Generation (RAG)-based LLM systems rely on external document corpora that can evolve and change over time. However, current evaluation methodologies (e.g., RAGAS) assess correctness against static snapshots, failing to detect faults when routine updates, factual changes, or noise alter the underlying data. We introduce a metamorphic testing framework that evaluates the consistency of RAG systems under corpus evolution. We formalise a fault taxonomy and 11 mutation operators that systematically perturb the system at both the pre-chunk (retrieval index) and post-chunk (retrieved context) levels. An empirical evaluation across five datasets and over 28k mutants reveals metamorphic violation rates of 4.9-10.2%. In a meta-evaluation against ground truth, our metamorphic oracle achieves F1 scores of 0.927-1.000, while the best RAGAS metric reaches only 0.570. Finally, we provide actionable insights into mitigating these faults through retrieval re-configuration, generator upgrades, and LLM-based reranking.
