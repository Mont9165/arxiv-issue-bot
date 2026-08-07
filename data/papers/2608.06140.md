# PLB: Priority-Aware Load Balancing for Replicated Databases under Constrained Resources

- arXiv ID: `2608.06140v1`
- Authors: Belkis Djeffal, Pierre Bourhis, Romain Rouvoy
- Published: 2026-08-06
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.DC`
- Links: [abs](http://arxiv.org/abs/2608.06140v1) | [pdf](https://arxiv.org/pdf/2608.06140v1)

## Abstract

Priority-differentiated services are a standard way for applications to offer different levels of performance, but database systems still often treat all sessions the same way. When database capacity is fixed, meaning replicas cannot be added on demand, and the workload becomes contended, this creates a difficult trade-off between over-provisioning resources and letting lower-priority users experience much larger slowdowns. In such settings, we propose enforcing priority by controlling how client sessions are assigned to database replicas.
  We present PLB, a priority-aware load balancer implemented as a JDBC driver that enforces priority differentiation through replica assignment under fixed resources. PLB partitions replicas by user group, premium versus freemium, and uses load-based borrowing so that higher-priority users can use idle capacity when available, while degradation for lower-priority users remains controlled. We evaluate PLB on a replicated read-only cluster under OLAP workloads. Compared with static dedicated per-priority partitions, PLB keeps utilization above about 70% in settings where fixed partitions can reduce cluster-wide CPU utilization to about 35%, while maintaining latencies close to those of the best dedicated allocation. Compared with a fully shared round-robin pool, PLB lowers high-priority median latency by about 12% on average, with improvements of up to 28%, while keeping the low-priority median overhead around 11% and overall median latency close to round-robin.
