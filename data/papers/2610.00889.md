# HakiCC: LLM-Driven Multi-Agent Design and Optimization of Concurrency Control Protocols

- arXiv ID: `2610.00889v1`
- Authors: Farzad Habibi, Juncheng Fang, Faisal Nawab
- Published: 2026-10-01
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.DC`, `cs.MA`
- Links: [abs](http://arxiv.org/abs/2610.00889v1) | [pdf](https://arxiv.org/pdf/2610.00889v1)

## Abstract

Large language models (LLMs) have recently been applied in systems research as a tool to reduce human-intensive engineering effort through cost-efficient automation. Decades of research have produced a rich landscape of concurrency control (CC) protocols, each encoding distinct trade-offs in correctness, throughput, and abort behavior. However, most applications in practice default to 2PL or OCC, because selecting and adapting a protocol to a specific application requires expert knowledge that is rarely available to application designers. This is a wasted opportunity, as an application-specific CC protocol can yield significant performance advantages over a generic baseline, but designing one requires deep expertise in CC protocol design.
  In this paper, we propose HakiCC, an LLM-driven multi-agent pipeline that automatically designs, verifies, and optimizes concurrency control protocols tailored to a given target application. HakiCC provides a two-stage pipeline. In Stage 1, a multi-agent system takes a workload description as input and generates an application-specific CC protocol implementation, which is iteratively repaired and verified for conflict-serializability. In Stage 2, the verified protocol is further optimized for that application through an LLM-driven evolutionary loop targeting correctness and throughput. We evaluate HakiCC on TPC-C and AuctionMark as target workloads, producing and reporting ten application-specific CC protocols. All ten are conflict-serializable after Stage 1; Stage 2 improves throughput for every protocol, with average gains of +50.6% for TPC-C protocols and +92.2% for AuctionMark protocols.
