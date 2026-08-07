# Debug Like a Human: Scaling LLM-based Fault Localization to Processor Design via Block-Level Instruction-Oriented Slicing

- arXiv ID: `2605.17290v1`
- Authors: Zizhen Liu, Xiaoguang Mao, Deheng Yang, Jiayu He, Yihao Qin, Guangda Zhang, Yan Lei, Jianjun Xu, Jiang Wu
- Published: 2026-05-17
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.17290v1) | [pdf](https://arxiv.org/pdf/2605.17290v1)

## Abstract

Fault localization in modern processor design code is a critical yet time-consuming step during processor verification. While recent advances in LLM-based techniques for module-level hardware design have shown promising results, automatically localizing bugs in large-scale, project-level processor designs remains challenging. In this paper, we present BluesFL, a novel block-level LLM-based fault localization framework for processor designs. Inspired by the way engineers debug processors, we first propose a dataflow-based code blockization approach to guide LLMs to focus on critical local code context. We further propose a Block-Level Instruction-Oriented Slicing (Blues) algorithm that enables LLMs to mimic human reasoning by analyzing instruction execution paths and processor states. We evaluate BluesFL on a real-world RISC-V processor core comprising 19K lines of SystemVerilog code. Experimental results demonstrate that BluesFL correctly localizes 24 bugs at Top-1, achieving 242.9% improvement over the existing state-of-the-art (7 bugs). Cost analysis shows that BluesFL requires an average of only $0.257 to localize a single bug.
