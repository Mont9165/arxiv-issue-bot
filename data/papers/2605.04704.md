# UVMarvel: an Automated LLM-aided UVM Machine for Subsystem-level RTL Verification

- arXiv ID: `2605.04704v1`
- Authors: Junhao Ye, Dingrong Pan, Hanyuan Liu, Yuchen Hu, Jie Zhou, Ke Xu, Xinwei Fang, Xi Wang, Nan Guan, Zhe Jiang
- Published: 2026-05-06
- Primary category: `cs.AR`
- Categories: `cs.AR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.04704v1) | [pdf](https://arxiv.org/pdf/2605.04704v1)

## Abstract

Verification presents a major bottleneck in Integrated Circuit (IC) development, consuming nearly 70% of total effort. While the Universal Verification Methodology (UVM) improves reuse through structured verification environments, constructing subsystem-level UVM testbenches and generating high-quality stimuli still require extensive manual coding, repeated EDA tool runs, and deep protocol and micro-architectural expertise. We present UVMarvel, an automated verification framework that leverages Large Language Models (LLMs) to build UVM testbenches for subsystem-level RTL.UVMarvel introduces an Intermediate Representation (IR) and a Bus Protocol Library to translate heterogeneous specifications into protocol-correct subsystem-level UVM testbenches, and employs a Signal Tracker and a Verilog Patching Library to guide LLM-based stimuli refinement. UVMarvel is the first framework capable of automatically constructing subsystem-level UVM testbenches across mainstream bus protocols, and it achieves an average code coverage of 95.65%, while reducing verification time from several human working days to a 4.5-hour automated execution.
