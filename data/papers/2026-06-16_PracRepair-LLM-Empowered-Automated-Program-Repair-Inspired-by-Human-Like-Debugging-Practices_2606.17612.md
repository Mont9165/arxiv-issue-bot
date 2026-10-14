# PracRepair: LLM-Empowered Automated Program Repair Inspired by Human-Like Debugging Practices

- arXiv ID: `2606.17612v1`
- Authors: Yu Cheng, Zhongxin Liu, Zhenchang Xing, Chao Ni, Qing Huang, Xiaoxue Ren
- Published: 2026-06-16
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.17612v1) | [pdf](https://arxiv.org/pdf/2606.17612v1)

## Abstract

As software systems grow in scale and complexity, debugging and repair remain costly and time-consuming. Large language models (LLMs) have advanced automated program repair (APR), but existing LLM-based APR approaches still largely rely on static or retrieved context, error messages, and coarse-grained validation outcomes. As a result, they underutilize dynamic information for failure understanding and repair, including failure-execution dynamics and patch-validation dynamics. Effectively leveraging such information, however, is challenging: failure-execution traces are large and noisy, raw static-dynamic context is not self-explanatory, and patch-validation dynamics are often reduced to coarse feedback. To address these challenges, we propose \textsc{PracRepair}, a fully automated LLM-based APR framework inspired by human-like debugging practices. \textsc{PracRepair} constructs an on-demand static-dynamic context from buggy programs and failure executions, performs question-driven failure diagnosis to formulate explicit repair hypotheses, and iteratively refines candidate patches using validation diagnostics and trace-level behavioral changes. Experimental results on Defects4J V1.2 and V2.0 show that \textsc{PracRepair} consistently outperforms state-of-the-art baselines. Specifically, under GPT-3.5, \textsc{PracRepair} correctly fixes 139/136 bugs on Defects4J V1.2/V2.0, while under GPT-4o it further improves to 162/171. Moreover, \textsc{PracRepair} generalizes effectively to RWB (Real-World Bugs), achieving the best performance across multiple foundation models.
