# VeriPilot: An LLM-Powered Verilog Debugging Framework

- arXiv ID: `2606.23759v1`
- Authors: Yihan Wang, Cheng Liu, Jiazheng Zhang, Lei Zhang, Long Cheng, Xiaowei Li, Huawei Li
- Published: 2026-06-22
- Primary category: `cs.AR`
- Categories: `cs.AR`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.23759v1) | [pdf](https://arxiv.org/pdf/2606.23759v1)

## Abstract

Verilog debugging remains one of the most time-consuming stages in digital circuit design. Recent advances in Large Language Models (LLMs) have enabled automated debugging; however, most existing approaches rely solely on test outputs and compiler feedback in an end-to-end manner, limiting their effectiveness on complex bugs. A key challenge is that the root cause of an error may be far removed from its observable outputs, making it difficult for LLMs to trace long dependency chains in code. This challenge is further exacerbated in large codebases, where long context lengths hinder efficient reasoning. To address these limitations, we propose VeriPilot, an LLM-powered debugging framework that leverages golden reference models to enable fine-grained bug localization and repair. VeriPilot goes beyond output-level comparison by aligning internal variable semantics between the Verilog design and its corresponding golden model through LLM-based analysis. It then performs step-by-step signal tracing using Control-Data-Flow Graphs (CDFGs) derived from static analysis, identifying a minimal set of suspicious code regions along with their correct counterparts from the golden model. These structured insights are subsequently provided to the LLM to guide reasoning and automated code repair. Experimental results on the Comprehensive Verilog Design Problems (CVDP) benchmark from NVIDIA demonstrate that VeriPilot improves the repair success rate of GPT-4o from 54.3\% to 85.71\%, significantly enhancing both bug localization accuracy and repair effectiveness for complex Verilog designs. The source code and benchmark are publicly available at Github https://github.com/YihanWn/VeriPilot.git.
