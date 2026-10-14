# Coverage Is Not Redundancy: Maintenance Cost and Exposure of Query-Aware Admission Indexes in Vector Databases Under Workload Drift

- arXiv ID: `2608.16043v1`
- Authors: Prashant Kumar Pathak
- Published: 2026-08-17
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2608.16043v1) | [pdf](https://arxiv.org/pdf/2608.16043v1)

## Abstract

In a vector database serving production-scale retrieval, a single inserted document can be retrieved for an anomalously large share of the query workload -- a retrieval hub -- and dominate the evidence returned for an entire topic. An emerging defense guards against this at ingest with an admission check: it maintains a set of sentinel queries and admits a document only if its reverse-kNN count against them stays below a threshold tau. Under workload drift this sentinel set is a query-aware auxiliary index that must be maintained online, and we study the cost that maintenance imposes on the ingest path. We identify a structural limit -- coverage is not redundancy: a monitor stops promoting sentinels once a region is covered, but the predicate rejects a hub only once tau sentinels witness it, so exposure has an observation-limited floor that no reduction in update or enforcement latency can close. On real HNSW, IVF-Flat, and IVF-PQ indexes over an 8.8M-vector MS MARCO corpus this floor is only a best case: as index recall falls, exposure and churn rise above it, and below recall ~0.5 the gate stops containing altogether -- worst on the memory-compressed IVF-PQ used at billion scale -- while a recall-aware witness probe restores containment at a fixed O(|S|d) admission cost, under 0.1% of the ANN insert. We validate the law under real (COVID-19) workload drift, implement the gate in PostgreSQL/pgvector at a 0.33% ingest tax, and turn the bound into a provisioning rule that sizes the sentinel budget per emerging region. A count test contains the hub where retrieval-time score normalizers (NNN, QB-Norm) do not, and a pre-registered causal suite isolates the missing-coverage mechanism from retrieval fragmentation across two embedding families (BGE-1024, E5-768).
