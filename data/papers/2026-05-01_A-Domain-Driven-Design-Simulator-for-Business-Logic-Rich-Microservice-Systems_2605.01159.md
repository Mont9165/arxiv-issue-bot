# A Domain-Driven Design Simulator for Business Logic-Rich Microservice Systems

- arXiv ID: `2605.01159v1`
- Authors: Daniel da Palma Pereira, António Rito Silva
- Published: 2026-05-01
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.DC`
- Links: [abs](http://arxiv.org/abs/2605.01159v1) | [pdf](https://arxiv.org/pdf/2605.01159v1)

## Abstract

Developing business-logic-rich microservices requires navigating complex trade-offs between data consistency and distributed coordination. Although patterns like Sagas and Transactional Causal Consistency (TCC) provide mechanisms to manage distributed state, validating their behavior before production is challenging. Current architectural simulators prioritize network metrics over domain semantics, whereas industry frameworks demand full-scale infrastructure deployments, preventing early architectural experimentation.
  To bridge this gap, we introduce a \textit{Domain-Driven Design} (DDD) microservice simulator that isolates core business logic from communication and transactional infrastructure. By modeling microservice systems around aggregates, the simulator allows developers to evaluate identical application code under varying consistency guarantees and network constraints. It features support for multiple transactional models (Sagas, TCC) and seamless transitions across diverse deployment topologies, ranging from centralized execution to fully distributed environments.
  We validate the simulator through the implementation and rigorous concurrency testing of a complex, multi-aggregate microservice system. Through empirical benchmarks, we quantify the performance, coordination overhead, and resilience of different transactional models across localized and distributed execution environments. The findings confirm that the simulator minimizes developer effort while providing a powerful, deterministic environment for the shift-left validation and optimization of business logic implementation in microservice architectures.
