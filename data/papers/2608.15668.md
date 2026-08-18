# An Empirical Comparison of Monolithic and Microservices Architectures for an E-Commerce Application

- arXiv ID: `2608.15668v1`
- Authors: Swayam Amol Katole
- Published: 2026-08-16
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.15668v1) | [pdf](https://arxiv.org/pdf/2608.15668v1)

## Abstract

Microservices architectures are widely adopted for their promised scalability and modularity, yet empirical evidence comparing their runtime performance to monolithic designs remains context-dependent. This paper presents an experimental comparison of a monolithic and a microservices implementation of the same e-commerce application, both backed by a shared PostgreSQL database. Using k6, we subject both systems to identical HTTP workloads at 50 and 100 virtual users (VUs) over 60-second runs, measuring throughput, latency, and error rates. At 50 VUs, both architectures perform similarly with no errors. At 100 VUs, the microservices design achieves 5.4% higher throughput, 25% lower average latency, and 39% lower p95 latency than the monolith, while exhibiting a lower median error rate (0.00% vs 0.69%). The monolith shows consistent order-creation failures under load, whereas microservices failures are transient and confined to the cart service in one run. These results suggest that, in this deployment context, decomposing the system into microservices improves scalability and tail latency under stress, while introducing distinct, service-specific failure modes that must be managed.
