# Harness Engineering in LLM Tool Use via Agent-Native Reusable Tool Primitives

- arXiv ID: `2609.01736v1`
- Authors: Haibo Jin, Suijin Wang, Xucheng Yu, Haojing Luo, Haohan Wang
- Published: 2026-09-01
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CL`, `cs.LG`, `cs.MA`
- Links: [abs](http://arxiv.org/abs/2609.01736v1) | [pdf](https://arxiv.org/pdf/2609.01736v1)

## Abstract

Large language models (LLMs) augmented with external tools have demonstrated remarkable capability in solving complex real-world tasks. However, existing approaches suffer from two key challenges: brittle multi-step and multi-turn reasoning caused by incompatible tool output types and API schemas, and performance degradation under large tool catalogues. To address these, we introduce \textbf{Tool Primitives}, a design that replaces rigid API schema-based invocation with natural language as the interface for tool calling, where each tool is wrapped with an LLM interface that handles schema resolution and execution internally, enabling natural inter-tool communication for nested and multi-turn tool calling. Building on Tool Primitives, we host \textbf{ToolFace}, a centralized repository of 25,519 functions from which LLMs dynamically retrieve only the relevant tools at inference time, eliminating the need to enumerate raw API schemas in context. To orchestrate Tool Primitives and ToolFace reliably in complex settings, we further propose \textbf{HEART}, a \textbf{H}arness \textbf{E}ngineering framework via \textbf{A}gent-native, \textbf{R}eusable \textbf{T}ool Primitives, comprising a Planner, Router, and Verifier that jointly support dynamic tool invocation planning, multi-step execution, and feedback-driven recovery.
  Experiments on five benchmarks demonstrate that HEART outperforms SFT-based models by $10\%$ on average and surpasses GPT-5.4, Claude-4.6-Sonnet, and Gemini-3.1-Pro by $6\%$ on average while reducing API cost by up to $85\%$. On 50 real-world tasks, HEART achieves $84\%$ task completion, $3.8\times$ the average of three frontier commercial models ($22\%$).
