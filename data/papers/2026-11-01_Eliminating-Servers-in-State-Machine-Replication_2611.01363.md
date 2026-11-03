# Eliminating Servers in State Machine Replication

- arXiv ID: `2611.01363v1`
- Authors: Dohyun Park, Wenjie Hu, Xiangyao Yu, Mahesh Balakrishnan, Yongjoo Park
- Published: 2026-11-01
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.DC`
- Links: [abs](http://arxiv.org/abs/2611.01363v1) | [pdf](https://arxiv.org/pdf/2611.01363v1)

## Abstract

State Machine Replication (SMR) underpins many stateful systems, including distributed databases, coordination services, and metadata stores. Fundamentally, SMR requires state to be materialized from a durable total order of commands. Existing SMR systems rely on servers to materialize, locally store, and serve snapshots of state; while the durable total order either resides on the same servers, or on an external, disaggregated shared log. Unfortunately, servers act as brittle, expensive choke-points in such systems, causing service unavailability when they fail; incurring provisioning latency on cold starts; and red-lining when exposed to bad clients. In this paper, we propose Serverless SMR (S^2MR), where both the materialized state and the durable total order are stored on disaggregated storage; clients concurrently maintain a single copy of materialized state on external storage. Our key technical insight is that the shared log abstraction is useful not just for consistently ordering commands in SMR, but also for enabling distributed materialization, thus becoming the only interface for ac hieving SMR. We demonstrate S^2MR by developing AirDB, a transactional key-value store. In our evaluation, AirD B over S^2MR achieves higher availability than existing SMR-based systems like etcd over Raft: it is oblivious to server failures and bad client activity; and spins up 10x-45x faster from a cold start.
