# Cassandra: Consensus with Partial Progress via Robust Partitionable View Synchronization

- arXiv ID: `2607.02856v1`
- Authors: Shaokang Xie, Dakai Kang, Junchao Chen, Suyash Gupta, Daniel P. Hughes, Mohammad Sadoghi
- Published: 2026-07-03
- Primary category: `cs.DC`
- Categories: `cs.DC`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.02856v1) | [pdf](https://arxiv.org/pdf/2607.02856v1)

## Abstract

Replicated databases and permissioned blockchain systems rely on Byzantine Fault-Tolerant (BFT) consensus to maintain a globally consistent order of transactions across distributed replicas. These protocols preserve safety even under asynchrony, as they commit a transaction only after agreement among a strong quorum of replicas. During network partitions, however, when no strong quorum is reachable, they lose liveness and cannot make useful progress.
  In this paper, we present Cassandra, a consensus protocol that enables partial progress without sacrificing safety. Cassandra achieves this through a two-tier certification framework that decouples availability from commitment, allowing each partition to extend its own chain and reconcile these chains once the network is restored. To support this, Cassandra introduces a pacemaker that advances views without requiring a strong quorum and calibrates each replica's timeout off the critical path.
  Our evaluation results show that Cassandra remains competitive with state-of-the-art BFT protocols under stable conditions, sustaining 900K TPS at 16 replicas and 480K TPS at 104 replicas, with latency ranging from 0.31s at 16 replicas to 0.75s at 104 replicas. Under severe partitions, Cassandra maintains non-zero speculative throughput through PoA-backed progress, preserving work that can be reconciled once connectivity is restored.
