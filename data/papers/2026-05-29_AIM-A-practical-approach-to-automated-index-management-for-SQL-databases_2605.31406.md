# AIM: A practical approach to automated index management for SQL databases

- arXiv ID: `2605.31406v1`
- Authors: Ritwik Yadav, Satyanarayana R. Valluri, Mohamed Zaït
- Published: 2026-05-29
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.31406v1) | [pdf](https://arxiv.org/pdf/2605.31406v1)

## Abstract

This paper describes AIM (Automatic Index Manager), a configurable index management system, which identifies impactful secondary indexes for SQL databases to efficiently use available resources such as CPU, I/O and storage. It has been validated on thousands of databases which support production systems. With AIM, the physical design of the database adapts itself to the changes in the workload.We lay out the end to end design of AIM while calling out the guarantees and tradeoffs associated with our design choices. Some of the salient features of AIM include fast convergence even while recommending wide composite indexes, reduced reliance on the query optimizer and a "no regression" guarantee for production workloads. Each index recommendation from AIM is accompanied with a metrics driven explanation, making it easier to verify machine driven changes.AIM is one of the few industrial strength index recommendation engines that is deployed on production databases at a large scale. The experimental results show that AIM is quick in identifying the most effective indexes and the resulting physical design is close to optimal.
