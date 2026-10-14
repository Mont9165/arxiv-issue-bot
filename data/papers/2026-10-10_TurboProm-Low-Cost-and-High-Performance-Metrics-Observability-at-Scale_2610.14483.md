# TurboProm: Low Cost and High Performance Metrics Observability at Scale

- arXiv ID: `2610.14483v1`
- Authors: Milind Srivastava, Zeying Zhu, Peilin Xin, Yancheng Yuan, Zaoxing Liu, Vyas Sekar
- Published: 2026-10-10
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.DC`, `cs.NI`
- Links: [abs](http://arxiv.org/abs/2610.14483v1) | [pdf](https://arxiv.org/pdf/2610.14483v1)

## Abstract

Many large enterprise and cloud deployments rely on metrics observability solutions (e.g., Prometheus) to monitor key performance indicators of system health (e.g., CPU, memory, network, app-level statistics). Monitoring and analyzing these metrics presents a significant challenge in terms of cost-latency tradeoffs at scale. Ideally, system operators would like immediately deployable and backwards compatible solutions to improve the cost-latency tradeoffs without significant impact on the fidelity of their observability applications. Unfortunately, existing solutions including state-of-art timeseries databases and custom approximate querying solutions fail on one or more aspects.
  In this paper, we present the design and implementation of TurboProm, a backwards-compatible drop-in accelerator for metrics observability deployments. TurboProm recasts metrics analytics tasks using a semantic-preserving summary view rather than classical query-centric view. Instead of estimating query results on raw timeseries metrics data, TurboProm uses semantic-preserving summaries that enable high-fidelity analytics with significant cost-latency improvements. We present a practical implementation of TurboProm that can be retrofitted to any existing observability deployment. We evaluate TurboProm on diverse real and synthetic workloads against state-of-art solutions and show that it can provide significant reduction in query latency and cost. TurboProm is open-source at https://github.com/ProjectASAP/ASAPQuery.
