# CloudIR-Bench: A Benchmark for Root Cause Analysis and Mitigation of Cloud Incidents

- arXiv ID: `2610.29185v1`
- Authors: Hoang Tran, Huong Ha, Tri Dang, Jeffrey Chan, Hongyu Zhang
- Published: 2026-10-21
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.29185v1) | [pdf](https://arxiv.org/pdf/2610.29185v1)

## Abstract

Root cause analysis (RCA) and mitigation prediction are essential for incident management, enabling the identification of underlying causes of failures and ensuring the reliability of complex cloud-based systems. With rising incident volume and system complexity, incident reports have become a valuable resource for these tasks. Recent studies have shown promising results using Large Language Models (LLMs) to predict root causes and mitigation actions from textual descriptions in incident reports. Despite these advances, further progress is hindered by the lack of publicly available datasets; existing work relies on private data, which limits transparency, reproducibility, and generalization. To address this gap, we introduce CloudIR-Bench, the first publicly available benchmark providing a dataset and evaluation framework for incident report-based RCA and mitigation prediction. Curated from incident reports across five leading cloud-based systems, CloudIR-Bench captures a diverse range of real-world production scenarios representing authentic failures and engineers' reasoning. We also release an open-source evaluation framework that includes eight recent LLM-based approaches. Our comprehensive evaluation includes zero-shot and in-context learning experiments, along with a qualitative analysis to identify where and why LLMs fail. Benchmarking results reveal the capabilities and limitations of existing LLMs in this domain. The benchmark, including the dataset, framework and supplementary materials, is available at https://github.com/hoangtnm/CloudIR-Bench.
