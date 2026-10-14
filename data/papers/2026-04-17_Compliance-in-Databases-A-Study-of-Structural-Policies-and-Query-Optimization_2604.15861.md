# Compliance in Databases: A Study of Structural Policies and Query Optimization

- arXiv ID: `2604.15861v1`
- Authors: Ahana Pradhan, Srinivas Karthik, Imtiyazuddin Shaik, Srinivas Vivek
- Published: 2026-04-17
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2604.15861v1) | [pdf](https://arxiv.org/pdf/2604.15861v1)

## Abstract

Growing privacy regulations and internal governance mandates are driving demand for fine-grained, context-sensitive access control in data management systems. Among competing approaches, content-based access control -- where access decisions depend on the data values referenced by a query -- is becoming particularly prominent, and is supported directly in modern database engines. While simple content-based predicates often incur negligible overhead, increasingly rich policies can interact in subtle ways with query optimization, leading to significant and poorly understood performance variability. This paper investigates this gap by introducing a structural framework and expressive policy grammar for modelling content-based compliance policies and analysing their impact on query planning and execution in database systems. Building on this framework, we augment an analytical benchmark with structured policy workloads, enabling controlled evaluation of enforcement mechanisms and optimization strategies under combined query - policy workloads. Our experimental results show that policy structure has a decisive impact on optimizer behaviour and end-to-end performance, underscoring the need for policy-aware database and optimizer design.
