# VSpector: Specification-Driven Bug Detection for RISC-V CPUs

- arXiv ID: `2609.23517v1`
- Authors: Tianyu Jia, Zhaoyang Yu, Yuanliang Chen, Wei You, Jianjun Huang, Bin Liang
- Published: 2026-09-20
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AR`
- Links: [abs](http://arxiv.org/abs/2609.23517v1) | [pdf](https://arxiv.org/pdf/2609.23517v1)

## Abstract

Detecting RTL design bugs in open-source RISC-V CPU implementations is critical for ensuring system reliability. Traditional detection approaches inherently rely on predefined artifacts. In this paper, we leverage the official,natural-language RISC-V specifications as an effective information source for bug detection. We present VSpector, a specification-driven bug detection pipeline that directly checks whether CPU register-transfer level (RTL) implementations adhere to official specification rules, without requiring specialized construction of reference models, formal properties, or custom bug patterns. To resolve the key technical trade-off between broad context scope and model reasoning accuracy when using Large Language Models (LLMs), VSpector employs a stepwise context refinement scheme across a four-stage pipeline: rule extraction, implementation localization, candidate identification, and sequential violation auditing. We evaluate VSpector on two industrial-strength RISC-V CPUs, CVA6 and XiangShan. Out of 217 reported candidates, manual inspection confirmed 148 true violations, representing a 68.2% precision. These violations correspond to 73 distinct bugs, including 42 previously unknown bugs. In our comparative experiments, DiveFuzz, a state-of-the-art CPU fuzzer, detected none of these new bugs during 24-hour runs per CPU. All 42 new bugs have been reported upstream, with developers already fixing 19 and confirming an additional 11 (30 in total), demonstrating that specification-driven auditing is a practical and complementary strategy for CPU bug detection.
