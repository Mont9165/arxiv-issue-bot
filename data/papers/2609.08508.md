# WiDiff: Extracting Changes from Wikidata's Edit History

- arXiv ID: `2609.08508v1`
- Authors: Carolina Cortés, Lisa Ehrlinger, Lorena Etcheverry, Felix Naumann
- Published: 2026-09-08
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2609.08508v1) | [pdf](https://arxiv.org/pdf/2609.08508v1)

## Abstract

Knowledge graphs have become a key resource for integrating heterogeneous data and powering downstream tasks such as question answering, entity linking, and semantic search. They are built and maintained incrementally, either (i) fully automated, e.g., YAGO, (ii) semiautomatically with community oversight, e.g., DBpedia, or (iii) manually through collaborative editing, e.g., Wikidata. Understanding the evolution of knowledge graphs is essential as changes may reflect real-world updates, error corrections, or noise introduced by vandalism, all of which affect the reliability of downstream applications. Among openly available knowledge graphs, Wikidata is the most challenging case to study evolution, with over 120 million entities edited by humans and bots and an edit history spanning more than a decade. Although Wikidata exposes change data in various formats (e.g., periodic dumps and real-time event streams), none support analytical queries over the complete edit history. Therefore, we present WiDiff, a tool that extracts changes from Wikidata's complete edit history and provides a unified interface for large-scale analytical queries over it.
