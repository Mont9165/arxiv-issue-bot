# Cascadeability and the Realization Gap: An Empirical Study of LLM-Powered Semantic Filtering

- arXiv ID: `2611.23898v1`
- Authors: Nan Hou, Kangfei Zhao, Jiadong Xie, Jeffrey Xu Yu
- Published: 2026-11-18
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.23898v1) | [pdf](https://arxiv.org/pdf/2611.23898v1)

## Abstract

Semantic filters enable natural language predicates over unstructured documents, but evaluating every document with a large language model (LLM) oracle is expensive. Proxy cascades reduce oracle invocations using cheaper surrogates, but oracle reduction alone cannot distinguish proxy limitations from calibration bottlenecks and establish practical efficiency. We present a unified benchmark of four representative systems, which formulate query processing as a three-stage workflow comprising proxy construction, threshold calibration, and cascade inference, using a two-threshold acceptance rule. We introduce cascadeability: the maximum empirical oracle reduction attainable from fixed proxy scores at a specified accuracy target, computed retrospectively using complete oracle labels. We investigate 8 research questions, spanning proxy quality, end-to-end performance, workload sensitivities, and component ablations, and reveal our key findings accordingly. Comparing cascadeability with achieved oracle reduction yields a realization gap that, interpreted alongside accuracy, exposes distinct proxy and calibration bottlenecks. The benchmark and diagnostics support evaluation beyond oracle reduction and motivate joint proxy-calibration design, class-sensitive quality assessment, and end-to-end cost optimization. We release a dataset-query benchmark, containing 10 real-world workloads across various domains and difficulties, with annotations of two LLM families.
