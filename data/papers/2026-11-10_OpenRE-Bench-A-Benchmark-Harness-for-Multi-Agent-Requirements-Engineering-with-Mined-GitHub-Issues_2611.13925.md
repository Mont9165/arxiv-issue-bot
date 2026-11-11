# OpenRE-Bench: A Benchmark Harness for Multi-Agent Requirements Engineering with Mined GitHub Issues

- arXiv ID: `2611.13925v1`
- Authors: Haowei Cheng, Milhan Kim, Bowen Jiang, Weixing Zhang, Yuhong Fu, Zhixu Liu, Naoyasu Ubayashi, Hironori Washizaki
- Published: 2026-11-10
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.13925v1) | [pdf](https://arxiv.org/pdf/2611.13925v1)

## Abstract

OpenRE-Bench is an open-source benchmarking infrastructure for large language model (LLM) based multi-agent requirements-engineering (RE) frameworks. Such frameworks are increasingly common, but they use different agent roles, negotiation policies, and output shapes, and are typically evaluated on their own runtimes, metrics, and small sets of curated system descriptions, which makes fair, reproducible comparison difficult. OpenRE-Bench addresses this with four reusable pieces: a shared run harness with one input, phase-artifact, and metric contract; an adapter mechanism through which a framework joins by implementing a single adapter, leaving cases, metrics, and other adapters untouched; a reproducible GitHub issue-mining pipeline that grows the corpus from real feature requests; and a versioned case suite. As a demonstration, we mine 3,000 fetched issues across five projects (three languages, five domains) into five cases, package them with five hand-built cases as the compact v1.0 suite, and run three heterogeneous frameworks (MARE and iReDev as paper-faithful reimplementations, plus QUARE) under one protocol. OpenRE-Bench originated as the evaluation back-end of our QUARE study and has since been reused by two further studies of our group. It is released with a pinned environment, a Docker image, frozen API snapshots, a 651-test suite, and the full pool of 1,396 filtered issues behind the mined cases.
