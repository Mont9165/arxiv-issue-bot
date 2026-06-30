# A Multi-Dataset Benchmark for Evaluating LLM Agents in Microservice Failure Diagnosis

- arXiv ID: `2606.29193v1`
- Authors: Yuanhong Cai, Xiaohui Nie, Kanglin Yin, Changhua Pei, Yongqian Sun, Shenglin Zhang, Haibin Liu, Guiyang Liu, Xidao Wen, Fang Situ, Dan Pei
- Published: 2026-06-28
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.29193v1) | [pdf](https://arxiv.org/pdf/2606.29193v1)

## Abstract

LLM-based agents are reshaping microservice operations into AgentOps, where benchmarks are key to evaluating failure diagnosis over multimodal observability data. However, existing benchmarks remain largely outcome-oriented: they score only the final answer and fail to assess the systematic reasoning process in failure diagnosis. We address this gap by introducing two large-scale datasets (AIOps2025 and RCA100) under a reasoning-process evaluation paradigm that assesses agentic diagnostic capability along three dimensions: Localization (where the fault occurs), Identification (what type of fault it is), and Reason (whether the reasoning trace is grounded in relevant evidence). Together, the two datasets comprise over 500 expert-labeled failure cases across two representative microservice systems (HipsterShop and the OpenTelemetry Demo Store). They cover diverse fault scenarios across resource, network, runtime, middleware/database, and application-logic categories and provide fine-grained causal evidence to support agent learning and reasoning-process evaluation. Beyond scale and coverage, the datasets have been carefully labelled by domain experts and validated through large-scale competitions, supporting more than 6,000 participating teams. This makes them not only expert-labeled diagnostic datasets, but also competition-validated benchmarks for evaluating agentic failure diagnosis in real-world microservice environments. Datasets are available at https://www.aiops.cn/gitlab/aiops-live-benchmark/agenticopseval.
