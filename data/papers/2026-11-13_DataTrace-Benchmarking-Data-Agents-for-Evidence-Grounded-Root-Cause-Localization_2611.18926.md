# DataTrace: Benchmarking Data Agents for Evidence-Grounded Root-Cause Localization

- arXiv ID: `2611.18926v1`
- Authors: Tung Sum Thomas Kwok, Xiaotian Lin, Yuyu Luo
- Published: 2026-11-13
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.18926v1) | [pdf](https://arxiv.org/pdf/2611.18926v1)

## Abstract

Database agents diagnose pipeline failures, but a correct root cause is trustworthy only when it is supported by evidence the agent inspected. Existing benchmarks usually grade the final query or answer but fail to distinguish an evidence-based diagnosis from an unsupported correct answer. We introduce DataTrace, a benchmark for evidence-grounded root-cause localization over typed graphs of database artifacts. DataTrace uses controlled fault injection to derive root causes and evidence paths within 83 runnable environments without human annotations, and scores root-cause correctness and coverage of the supporting path separately. We also introduce CoSE, a generator-solver protocol in which an external verifier admits reproducible faults and checks both the submitted answer and the inspected evidence. Our evaluation shows that seven proprietary models achieve average root-cause accuracy 48%, with a mean per-model conditional unsupported rate of 18%. Fine-grained analysis shows that this gap varies sharply with fault mechanism, dependency distance, and evidence modality. After in-loop training on a matched held-out batch, the share of grounded correct diagnoses rises from 83.7% to 94.6%, while root-cause accuracy rises from 29.2% to 36.7%. These results show that while final-answer accuracy can hide unsupported diagnoses, evidence coverage provides an actionable signal to improve database agents. Code and data are available at https://hkustdial.github.io/datatrace/.
