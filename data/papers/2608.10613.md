# CausalRepair: Bridging the Causality Gap in Large Language Model-Based Automated Program Repair via Dual-Slicing

- arXiv ID: `2608.10613v1`
- Authors: Linhao Wu, Yizhou Chen, Zhen Yang, Pengyu Xue, Dan Hao
- Published: 2026-08-11
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.10613v1) | [pdf](https://arxiv.org/pdf/2608.10613v1)

## Abstract

Automated Program Repair (APR) has recently benefited from Large Language Models (LLMs), yet their effectiveness heavily depends on repair context. Existing LLM-based APR methods suffer from a causality gap: test contexts can be noisy or incomplete, while source contexts derived from static analysis often contain irrelevant and unexecuted code, misleading LLMs from identifying the true root cause. To address this issue, we propose CausalRepair, a conversation-driven APR framework based on minimal causal context, i.e., the essential dependencies required to explain a failure. CausalRepair employs a dual-slicing strategy: context-aware static slicing purifies test semantics, while execution-trace-based dynamic slicing captures precise runtime dependencies in source code. Together, they construct compact, causally relevant contexts to guide iterative repair. We evaluate CausalRepair on Defects4J V1.2, V2.0, and Defects4J-Trans using DeepSeek-V3. CausalRepair correctly fixes 313 bugs on Defects4J, outperforming state-of-the-art approaches such as ReinFix and TSAPR, while reducing the average repair cost to $0.029 per bug.
