# TripleBound: Triplet-Guided Heterogeneous Graph Learning for Microservice Decomposition

- arXiv ID: `2609.11212v1`
- Authors: Mineth Weerasinghe, Himindu Kularathne, Methmini Madhushika, Danuka Lakshan, Nisansa de Silva, Adeesha Wijayasiri, Srinath Perera
- Published: 2026-09-10
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.11212v1) | [pdf](https://arxiv.org/pdf/2609.11212v1)

## Abstract

Cloud computing and DevOps have made microservices a common architecture for scalable, maintainable software systems. However, migrating monoliths to microservices remains challenging due to tight coupling and unclear service boundaries. Existing decomposition approaches typically rely on either structural dependencies or semantic similarity signals, but rarely integrate both within a unified representation learning objective. This paper proposes TripleBound, a hybrid framework for automated monolith-to-microservices decomposition that augments a heterogeneous graph neural network with weakly supervised triplet constraints derived from parser-inferred service groups based on package structure, naming conventions, and code location. TripleBound injects triplet-based constraints directly into the shared structural latent space, enabling both signals to be jointly optimized during representation learning. Structural dependencies are captured using CHGNN, which models the monolith as a heterogeneous graph with program nodes, resource nodes, CALL edges, and CRUD edges. Semantic relationships are incorporated through triplet constraints generated from parser-inferred service groups. Evaluation on AcmeAir, DayTrader, PlantsByWebSphere, and JPetStore shows that TripleBound achieves the highest composite decomposition score under the selected weighting on AcmeAir, DayTrader, and JPetStore compared to CHGNN and MonoEmbed, while CHGNN remains stronger on PlantsByWebSphere. Per-metric analysis reveals trade-offs: gains in structural modularity and inter-partition coupling are accompanied by higher entity distribution imbalance on some datasets. Alternative composite weightings preserve TripleBound's first-place ranking on AcmeAir and DayTrader but not on JPetStore, showing that the aggregate ranking is metric-dependent.
