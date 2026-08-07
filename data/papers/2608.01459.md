# Six Dimensions of Benchmarking Time-Series Databases

- arXiv ID: `2608.01459v1`
- Authors: Jalal Mostafa, Sandro Melissano, Nicholas Tan Jerome, Suren Chilingaryan, Andreas Kopmann
- Published: 2026-08-02
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.01459v1) | [pdf](https://arxiv.org/pdf/2608.01459v1)

## Abstract

Time-series databases (TSDBs) employ diverse storage architectures optimized for specific workload characteristics, leading to distinct performance profiles and bottlenecks that are often not apparent under conventional benchmarking approaches. System architects designing robust data backends must understand which storage engines are efficient for their particular pipelines and which exhibit the lowest risk of encountering future scalability constraints. This paper presents SciTSv2, a benchmarking framework that evaluates time-series databases across six workload dimensions: connection parallelism, batch ingestion, time-series regularity, multi-variate series, mixed workloads, and system metrics. We exploit SciTSv2 to systematically evaluate 4 TSDBs representing distinct storage engines: InfluxDB (Time-Structured Merge tree), TimescaleDB (based on relational databases), ClickHouse (columnar), and DataLayerTS (specialized in regular time-series). We show that each dimension surfaces architectural behavior that dedicated, single-axis benchmarks obscure, including regularity-dependent trade-offs, contention between concurrent reads and writes, and distinct CPU, I/O, and disk-bandwidth-bound bottlenecks. Paired with fine-grained system metrics, SciTSv2 gives architects a diagnostic tool for tracing performance outcomes back to their underlying architectural causes, supporting storage engine selections grounded in empirical, workload-specific evidence.
