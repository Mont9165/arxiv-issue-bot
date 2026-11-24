# SYCLDB: A Cross-Vendor Heterogeneous Analytical DBMS

- arXiv ID: `2611.30849v1`
- Authors: Ivan Donchev Kabadzhov, Eugenio Marinelli, Raja Appuswamy
- Published: 2026-11-23
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.DC`
- Links: [abs](http://arxiv.org/abs/2611.30849v1) | [pdf](https://arxiv.org/pdf/2611.30849v1)

## Abstract

The rapid growth of AI and analytical workloads has increased the need for fast, interactive analytical data processing. This, in turn, has led to a surge of interest in designing accelerated analytical database engines that can exploit modern GPUs to scale computation. While GPUs provide the massive data-parallelism required by modern analytics, the software landscape remains dominated by closed-source, vendor-locked programming models, like CUDA, limiting portability across multi-vendor GPUs. In this work, we present SYCLDB, an end-to-end analytical database engine built upon the SYCL open standard, designed to enable efficient, hardware-agnostic execution across a wide range of accelerators using a single codebase. By implementing core relational operators as modular SYCL kernels, integrating them with a SQL frontend based on Apache Calcite and Apache Thrift, and supporting Apache Arrow for efficient columnar ingestion, SYCLDB reduces dependence on vendor-specific GPU programming stacks by enabling a single SYCL codebase to execute analytical query pipelines across Intel, AMD, and NVIDIA GPUs.
