# Genetic Programming for Self-Adaptive Auto-Scaling of Microservices

- arXiv ID: `2605.01533v1`
- Authors: Jia Li, Mehrdad Sabetzadeh, Shiva Nejati
- Published: 2026-05-02
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.01533v1) | [pdf](https://arxiv.org/pdf/2605.01533v1)

## Abstract

Microservice architecture is widely adopted in modern systems, where auto-scaling is critical for satisfying service-level objectives (SLOs). However, determining optimal scaling for microservices is difficult, and reactive resource allocation often leads to costly over- or under-provisioning. We propose AutoSLO, a learning-based, self-adaptive scaling framework that dynamically adjusts microservice replicas to meet SLOs while minimizing resource usage. AutoSLO uses a continuous monitoring-adaptation feedback loop and leverages genetic programming to learn and evolve scaling logic, enabling the deployed microservice system to proactively prevent SLO violations rather than repeatedly searching for one-off scaling actions. We evaluate AutoSLO on two case-study systems -- an online shopping platform and a chatbot based on large language models -- and show that this framework substantially reduces resource usage while maintaining a low frequency of SLO violations, all of which are resolved within a short time window.
