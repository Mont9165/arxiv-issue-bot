# Deterministic vs. LLM-Controlled Orchestration for COBOL-to-Python Modernization

- arXiv ID: `2605.09894v1`
- Authors: Naing Oo Lwin, Rajesh Kumar
- Published: 2026-05-11
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.MA`
- Links: [abs](http://arxiv.org/abs/2605.09894v1) | [pdf](https://arxiv.org/pdf/2605.09894v1)

## Abstract

Modernizing legacy COBOL systems remains difficult due to scarce expertise, large and long-lived codebases, and strict correctness requirements. Recent large language model (LLM)-based modernization systems increasingly rely on agentic workflows in which the model controls multi-step tool execution. However, it remains unclear whether delegating execution control to the LLM improves correctness, robustness, or efficiency in structured software engineering workflows. We present a controlled empirical study of deterministic and LLM-controlled orchestration for COBOL-to-Python modernization. Using a unified experimental framework, we hold the language models, prompts, tools, configurations, and source programs constant while varying only the execution control strategy. This isolates orchestration as the sole experimental variable. We evaluate both approaches using functional correctness, robustness across repeated stochastic runs, and computational efficiency. Across multiple models, deterministic orchestration achieves comparable computational accuracy to LLM-controlled orchestration while improving worst-case robustness and reducing performance variability across runs. Deterministic execution also reduces token consumption by up to 3.5x, leading to substantially lower operational cost. These results suggest that, in structured modernization workflows with explicit validation stages, fixed execution policies provide more stable and cost-efficient behavior than fully agentic orchestration without reducing translation quality.
