# Living Databases: A Unified Model for Continuous Schema Evolution, Versioning, and Transformations

- arXiv ID: `2605.00676v1`
- Authors: Amol Deshpande
- Published: 2026-05-01
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.00676v1) | [pdf](https://arxiv.org/pdf/2605.00676v1)

## Abstract

Databases, and datasets more generally, evolve continuously through updates, transformations, versioning, schema changes, streaming operations, and other mechanisms. While prior work has noted connections among some of these areas, they have traditionally been studied in isolation, each with its own abstractions, algorithms, and system implementations. In this paper, we argue for unifying these diverse functionalities under a single abstraction and a common set of computational primitives. We present such an abstraction, powerful enough to encompass existing use cases and to support new ones. Going beyond previous approaches, our framework seamlessly integrates provenance tracking for system-visible operations, conditional propagation of updates, and configurable alerts on change events. It also offers a principled treatment of dependent objects such as views and derived artifacts like machine learning models, by providing declarative mechanisms to control their evolution. Finally, we sketch a prototype implementation in a relational-like database system based on an adaptation of the "Prolly Tree", a Merkle tree-inspired data structure with tunable parameters to meet varying performance requirements, and present some initial experimental results.
