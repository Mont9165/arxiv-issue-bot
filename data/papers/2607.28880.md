# LayoutBench: Performance Benchmarking of Cloud Storage Layouts for Multimedia Data

- arXiv ID: `2607.28880v1`
- Authors: Debopam Sanyal, Hongjie Chen, Alexey Tumanov, Joshua Kimball
- Published: 2026-07-30
- Primary category: `cs.DC`
- Categories: `cs.DC`, `cs.DB`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2607.28880v1) | [pdf](https://arxiv.org/pdf/2607.28880v1)

## Abstract

Modern multimedia machine learning workloads increasingly store large-scale datasets in cloud object storage services such as AWS S3. How these samples are physically organized in storage (i.e.,storage layout) directly affects how quickly and cheaply they can be retrieved. Yet the benchmarks used to guide storage decisions today focus on database engines and query processing, and none systematically evaluates how different storage layouts perform for multimedia data retrieval. We present LayoutBench, the first benchmark designed to fill this gap. It evaluates three representative layout strategies: storing each sample as an individual object (L1), sequentially packing samples into tar archives (L2), and organizing samples as columns in Parquet files (L3). We measure retrieval time, data transferred, and monetary cost using 11 queries of varying result-set sizes on ImageNet across six AWS EC2 instance configurations that span different network bandwidth and memory tiers. Our experiments reveal that L2 achieves lower latency than L1 and L3 through connection reuse, but loses this advantage as retrieval sizes become very large. L3 is the fastest for very large retrievals but transfers substantially more data across all query sizes due to row-group granularity, and requires significantly more memory. Across all layouts, data transfer cost dominates total expenditure, with L3 costing an order of magnitude more than L1 or L2.
