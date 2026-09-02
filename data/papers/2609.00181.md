# Intelligent Edge Computing

- arXiv ID: `2609.00181v1`
- Authors: Kalgi Gandhi, Minal Bhise
- Published: 2026-08-31
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.00181v1) | [pdf](https://arxiv.org/pdf/2609.00181v1)

## Abstract

The number of edge devices in large-scale edge systems is rapidly increasing. Edge devices have limited processing power, memory, and network bandwidth, making resource utilization and data management during edge query processing challenging. Joins are among the costliest database operations in terms of time and resources. The State-of-the-Art edge query processing, Column Imprint-Hash Join CI-HJ, addresses this challenge using equi-height binning to accelerate hash joins. However, it lacks efficiency in real-time processing and scans unnecessary cachelines. This paper presents Workload Aware Column Imprint-Hash Join WACI-HJ, which uses a workload-aware approach to accelerate hash joins. Predicting the upcoming query workload in advance further improves its suitability for real-time edge query processing. WACI-HJ comprises two phases: WACI-HJ Generation Phase, including Pre-processing, Prediction, and Blocking and Hashing modules to compute bins based on the predicted workload before query arrival, and Query Processing and Resource Utilization, which handles query processing and CPU, RAM, and I/O utilization. Evaluations on a benchmark dataset and a real-world Smart Transportation dataset show a 54% reduction in cachelines read and 10% improved query execution time. The proposed technique is effective for both scaled and skewed data. Although PCR is an indirect measure of energy consumption, the work also directly measures energy consumption through energy-efficiency experiments. WACI-HJ shows 1%, 38%, and 49% gain in CPU, RAM, and I/O, respectively. Optimizing cache usage and query execution speeds up real-time traffic analysis, congestion management, and routing in Smart Transportation. Additionally, this technology can be applied to other domains to accelerate edge query processing.
