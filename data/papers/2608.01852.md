# Multimodal Embeddings for 3D Similarity Search in Semantic Web-of-Things Digital-Twin Platforms

- arXiv ID: `2608.01852v1`
- Authors: Oussama Zaid, Romaric Gaudel, Hassan Thomas, Maria Massri, Philippe Raipin-Parv{é}dy
- Published: 2026-08-03
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2608.01852v1) | [pdf](https://arxiv.org/pdf/2608.01852v1)

## Abstract

Semantic Web of Things (SWoT) platforms model physical infrastructure as knowledge graphs typed against domain ontologies, enabling expressive structural and logical queries. However, they lack native mechanisms to express similarity beyond strict ontological equivalence, which represents a critical gap for 3D digital twins in domains such as telecom infrastructure and industrial IoT, where queries must combine ontological constraints with multimodal similarity search over heterogeneous, temporally-evolving scene data. We propose a framework that extends SWoT platforms with a multimodal embedding layer: ontology-typed entities comprising 3D point clouds, temporal attributes, and semantic labels are encoded into latent vector representations stored alongside the knowledge graph, enabling hybrid ontology-vector queries that combine graph-based filtering with similarity search. Implemented on Orange Research's Thing'in platform with the Clock-G temporal graph database, a feasibility evaluation on S3DIS demonstrates that graph filtering effectively restricts the search pool under temporal and relational constraints, and that general-purpose pretrained encoders produce representations sufficient for similarity retrieval and as a preliminary encoding step for downstream predictive tasks.
