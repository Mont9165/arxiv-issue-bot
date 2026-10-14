# QBugLM: An Agentic Benchmarking Framework for LLM-based Quantum Software Debugging

- arXiv ID: `2606.07314v1`
- Authors: An B. B. Pham, Hoa T. Nguyen, Muhammad Usman
- Published: 2026-06-05
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.ET`, `quant-ph`
- Links: [abs](http://arxiv.org/abs/2606.07314v1) | [pdf](https://arxiv.org/pdf/2606.07314v1)

## Abstract

Quantum software bugs often yield silent, incorrect outputs rather than explicit errors, making them particularly difficult to detect and repair with conventional techniques. Although large language models (LLMs) have shown strong performance on classical software engineering tasks, their ability to debug quantum code remains largely unexplored. To bridge this gap, we propose QBugLM, a multi-agent framework that automates the quantum software debugging pipeline, from taxonomy-driven bug injection to LLM-based detection and repair, and finally to simulation-based validation, for framework-agnostic OpenQASM 3.0 programs. We further conduct a comprehensive case study using QBugLM to benchmark two LLMs, Claude 4.6 Sonnet and Qwen3 Coder Next, across different prompting strategies, bug categories, and quantum programs. Our results show that iterative feedback is critical, as a single retry raises Pass@1 from below 25% to above 80%. Moreover, simpler structured prompting can even outperform Chain-of-Thought and ReAct for reasoning-capable models under fixed-resource constraints. Our work takes initial steps toward benchmarking LLM capabilities for debugging quantum programs and offers practical insights to support future efforts in automated quantum software repair.
